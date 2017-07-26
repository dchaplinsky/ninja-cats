# ninja-cats
Mysterious ninja-cats that appears from thin air to help


# Installation
Install all the bleeding-edge deps:
```
pip install -r requirements.txt
```
Or install it from local disk, if you already have them:
```
pip install -r requirements_local.txt
```

create `local_settings.py`:
```
cp local_settings.py.template local_settings.py
```

and add some `SOCIAL_AUTH_*` in there.

Then `run`.

# Docker

First build the image (mongo, python3.6, ruby/sass)
```
docker build -t ninja-cats/vulyk-env .
```

Then `run`:

```
docker run -p 5000:5000 -it -v $(pwd):/var/task --rm  ninja-cats/vulyk-env bash -c "cd /var/task; bash run_in_docker.sh"
```
and open `http://localhost:5000/` in your browser.