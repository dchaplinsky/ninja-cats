FROM python:3.7.2-alpine3.8

ARG root=/app

LABEL kind=app

WORKDIR ${root}

ENV PYTHONPATH=${root} PREFIX=${root} \
		STATIC_ROOT=${root}/static MEDIA_ROOT=/media \
		APP_NAME="run:app" APP_WORKERS="2"

RUN /usr/sbin/adduser -D -h ${root} app

COPY ./requirements.txt ${root}/requirements.txt

RUN apk add --no-cache su-exec postgresql-libs libjpeg sassc \
		&& ln -sf /usr/bin/sassc /usr/bin/sccs \
		&& apk add --no-cache --virtual .build-deps jpeg-dev zlib-dev postgresql-dev build-base git

RUN PREFIX=/usr/local pip install -r  ${root}/requirements.txt

RUN runDeps="$( \
			scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \
				| tr ',' '\n' \
				| sort -u \
				| awk 'system("[ -e /usr/local/lib" $1 " ]") == 0 { next } { print "so:" $1 }' \
		)" \
			apk add --no-cache --virtual .app-rundeps $runDeps \
		&& apk del .build-deps

COPY . ${root}/
COPY docker-entrypoint.sh /usr/local/bin/

RUN python -m compileall ${root} \
		&& mkdir -p ${MEDIA_ROOT} \
		&& mkdir -p /var/log/vulyk \
		&& FLASK_APP=run.py flask assets build \
		&& chown app -R /var/log/vulyk ${STATIC_ROOT} \
		&& mv local_settings.py.template local_settings.py

ENTRYPOINT [ "docker-entrypoint.sh" ]

VOLUME [ "${STATIC_ROOT}", "${MEDIA_ROOT}" ]

EXPOSE 8000

CMD [ "gunicorn" ]
