# demo-jukebox-api

Demo jukebox API

Song credits: https://freepd.com

### Run

#### Using code (local)

```sh
# Ensure python 2.x and pip installed
pip install -r app/requirements.txt
python app/server.py
```

#### Using docker

```sh
docker run -p 5000:5000 -p 8000:8000 endeepak/demo-jukebox-api
```

### API

```sh
$ curl localhost:5000/api/songs/random
```

### Metrics

Metrics will available in http://localhost:8000
