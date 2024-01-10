# Watcher for count clients online

## Install

1. Clone repositories

```shell
git clone https://github.com/drlenux/online-watcher.git
```

2. install docker and docker-compose
3. change `passwd` in [app/config.yml](./app/config.yml)
4. change `port` in [Dockerfile (line: 11)](./Dockerfile)  
5. run `docker-compose up -d` (or rewrite [this code](./docker-compose.yml))

## Use

### url for clients

```shell
http://0.0.0.0:8080/ping
```

### url for check count online

```shell
http://0.0.0.0:80/count/[passwd]
```