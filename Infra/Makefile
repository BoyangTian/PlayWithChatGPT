# Define variables
PYTHON = python3
PROJECT_NAME = Infra
VERSION=0.0.1

all: help

help:
	@echo "db             		- Start postgres db."
	@echo "dbstop             	- Stop postgres db."
	@echo "dblogin             	- Login to db instance."
	@echo "dblog             	- Tail 50 log for db instance."

db:
	docker-compose -f postgres/docker-compose.yml up -d

dbstop:
	docker-compose -f postgres/docker-compose.yml down

dblogin:
	docker-compose -f postgres/docker-compose.yml exec db-postgres-simplesite psql -U admin -d simplesite

dblog:
	docker-compose -f postgres/docker-compose.yml logs --tail 50

.PHONY: db
