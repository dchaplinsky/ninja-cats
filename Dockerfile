FROM python:3.7.2-alpine3.8

ARG root=/app

LABEL kind=app

WORKDIR ${root}

ENV PYTHONPATH=${root} PREFIX=${root} \
		STATIC_ROOT=${root}/static STATIC_ROOT_SOURCE=/static MEDIA_ROOT=/media \
		LOG_ROOT=/var/log/vulyk \
		APP_NAME="run:app" APP_WORKERS="2"

RUN /usr/sbin/adduser -D -h ${root} app

COPY ./requirements.txt ${root}/requirements.txt

RUN apk add --no-cache su-exec postgresql-libs libjpeg ruby \
		&& apk add --no-cache --virtual .build-deps jpeg-dev zlib-dev \
					postgresql-dev build-base git ruby-dev ruby-rdoc \
		&& PREFIX=/usr/local pip install -r  ${root}/requirements.txt \
		&& PREFIX=/usr gem install sass \
		&& runDeps="$( \
			scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \
				| tr ',' '\n' \
				| sort -u \
				| awk 'system("[ -e /usr/local/lib" $1 " ]") == 0 { next } { print "so:" $1 }' \
		)" \
			apk add --no-cache --virtual .app-rundeps $runDeps \
		&& apk del .build-deps

COPY . ${root}/
COPY docker-entrypoint.sh /usr/local/bin/

RUN rm -f docker-entrypoint.sh \
		&& python -m compileall ${root} \
		&& mkdir -p ${MEDIA_ROOT} ${STATIC_ROOT_SOURCE} ${LOG_ROOT} \
		# build static in the STATIC_ROOT and then move to STATIC_ROOT_SOURCE
		# then before start copy all these files over host-mounted STATIC_ROOT
		&& FLASK_APP=run.py flask assets build \
		&& mv ${STATIC_ROOT}/* ${STATIC_ROOT_SOURCE}/ \
		&& chown app -R ${LOG_ROOT} ${STATIC_ROOT} \
		&& mv local_settings.py.template local_settings.py

ENTRYPOINT [ "docker-entrypoint.sh" ]

VOLUME [ "${STATIC_ROOT}", "${MEDIA_ROOT}" ]

EXPOSE 8000

CMD [ "gunicorn" ]
