# Watcher for Counting Clients Online

## Installation:

1. Clone repositories:

```shell
git clone https://github.com/drlenux/online-watcher.git
```

2. Install Docker and Docker-compose or Python 3.9 and dependencies.
3. Change `access` and `life_time` in [app/config.yml](./app/config.yml) 

## Running the Application:
- Using Docker-compose:
```shell
make up
```
(Note: Change the port in [Dockerfile](./Dockerfile) and [docker-compose.yml](./docker-compose.yml).)
- Using Python on your server (require installing [requirements](./requirements.txt)):
```shell
make run
```

(Note: Change the `port` and `IP` in [Makefile](./Makefile).)

## Usage:

- URL for clients to ping:

```shell
http://0.0.0.0:8080/ping
```

- URL to check the count of online users:

```shell
http://0.0.0.0:80/count/user
```
(Add Basic Authentication.)

- URL to check the count of hits:

```shell
http://0.0.0.0:80/count/hits
```

(Add Basic Authentication.)