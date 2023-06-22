# Define variables
PYTHON = python3
PROJECT_NAME = Infra
VERSION=0.0.1

all: help

help:
	@echo "db             		- Start postgres db."
	@echo "dbstop             	- Stop postgres db without stop network associate to it."
	@echo "dblogin             	- Login to db instance."
	@echo "dblog             	- Tail 50 log for db instance."
	@echo "simplesite           - Start Django simplesite application with postgresql docker container"
	@echo "down             	- Down all services."

db:
	docker-compose -f postgres/docker-compose.yml up -d db-postgres-simplesite

# there is no way to just "down" one service. Therefore we can only use "stop" command.
# but it will not stop the network associate to this service
# https://forums.docker.com/t/docker-compose-down-specific-service/125914/4
dbstop:
	docker-compose -f postgres/docker-compose.yml stop db-postgres-simplesite

dblogin:
	docker-compose -f postgres/docker-compose.yml exec db-postgres-simplesite psql -U admin -d simplesite

dblog:
	docker-compose -f postgres/docker-compose.yml logs --tail 50

simplesite:
	docker-compose -f postgres/docker-compose.yml -f django-simplesite/docker-compose.yml up -d

down:
	docker-compose -f postgres/docker-compose.yml -f django-simplesite/docker-compose.yml down

.PHONY: db
