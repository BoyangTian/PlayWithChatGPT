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
	$(if $(DB_NAME),,$(error DB_NAME is not defined. Please provide a value when running the command, e.g., make test DB_NAME=<value>))
	docker-compose -f postgres/docker-compose.yml up -d db-postgres-$(DB_NAME)

db-all:
	docker-compose -f postgres/docker-compose.yml up -d

# there is no way to just "down" one service. Therefore we can only use "stop" command.
# but it will not stop the network associate to this service
# https://forums.docker.com/t/docker-compose-down-specific-service/125914/4
dbstop:
	$(if $(DB_NAME),,$(error DB_NAME is not defined. Please provide a value when running the command, e.g., make test DB_NAME=<value>))
	docker-compose -f postgres/docker-compose.yml stop db-postgres-$(DB_NAME)

dblogin:
	$(if $(DB_NAME),,$(error DB_NAME is not defined. Please provide a value when running the command, e.g., make test DB_NAME=<value> PORT=<value>))
	$(if $(PORT),,$(error DB_NAME is not defined. Please provide a value when running the command, e.g., make test DB_NAME=<value> PORT=<value>))
	docker-compose -f postgres/docker-compose.yml exec db-postgres-${DB_NAME} psql -U admin_$(DB_NAME) -d $(DB_NAME) -p $(PORT)

dblog:
	$(if $(DB_NAME),,$(error DB_NAME is not defined. Please provide a value when running the command, e.g., make test DB_NAME=<value>))
	docker-compose -f postgres/docker-compose.yml logs --tail 50 db-postgres-$(DB_NAME)

simplesite:
	docker-compose -f postgres/docker-compose.yml -f django-simplesite/docker-compose.yml up -d

down:
	docker-compose -f postgres/docker-compose.yml -f django-simplesite/docker-compose.yml down

.PHONY: db
