run:
	./.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload --proxy-headers

build:
	docker-compose build server

up:
	docker-compose up -d

down:
	docker-compose down