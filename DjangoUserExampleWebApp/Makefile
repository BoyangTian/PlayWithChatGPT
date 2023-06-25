# Define variables
PYTHON = python3
PROJECT_NAME = DjangoUserExampleWebApp
include usersite.env
VERSION=${TAG}
PYTHON_VERSION=3.9.6
# Define the activate and deactivate commands for Pyenv
PYENV_INSTALL = pyenv install -s $(PYTHON_VERSION)
PYENV_ACTIVATE = pyenv local $(PROJECT_NAME)
PYENV_DEACTIVATE = source deactivate $(PROJECT_NAME)
PIP_REQUIREMENTS=requirements.txt

.DEFAULT_GOAL := run

all: help

help:
	@echo "activate             		- Pyenv activate."
	@echo "deactivate           		- Pyenv deactivate."
	@echo "install              		- Install from requirements."
	@echo "django-shell         		- Run python with django dependencies."
	@echo "run                  		- Run."
	@echo "migration-check      		- Before update DB check schema update."
	@echo "migration-update-detail  	- Get detail of update DB schema before migrate."
	@echo "test TEST_MODEL=<model>  	- Test specific model."
	@echo "test-all                		- Test all."
	@echo "create-app APP_NAME=<value>	- Create sub app under usersite folder."
	@echo "clean                		- Clean python cache."

# Activate the Pyenv virtual environment
activate:
	$(PYENV_INSTALL) && \
	if ! pyenv virtualenvs | grep -q $(PROJECT_NAME); then \
		pyenv virtualenv $(PYTHON_VERSION) $(PROJECT_NAME); \
	fi
	$(PYENV_ACTIVATE) && \
	echo "Activated Pyenv virtual environment '$(PROJECT_NAME)' with Python $(PYTHON_VERSION)"

# Deactivate the Pyenv virtual environment
# TODO: not work correctly, still shows same version when run: pyenv versions
# In order to totally delet it, need to run: make clean
deactivate:
	$(PYENV_DEACTIVATE) && \
	echo "Deactivated Pyenv virtual environment '$(PROJECT_NAME)' result with $?"

# TODO: not work: Install required packages that are not already installed
# pip install $(grep -v '^#' requirements.txt | grep -vxFf <(pip freeze) | cut -d= -f1)
# The pip install command installs the packages that are not already installed.
# grep -v '^#' requirements.txt removes any comments from requirements.txt (lines starting with #).
# grep -vxFf <(pip freeze) removes any packages that are already installed. pip freeze lists all installed packages and grep -vxFf removes any lines that match packages in the requirements.txt file.
# cut -d= -f1 removes the version information from the package names, leaving only the package names themselves.
install: activate
	pip install -r requirements.txt && \
	echo "Installed dependencies"

migration: install
	$(PYTHON) usersite/manage.py makemigrations
	$(PYTHON) usersite/manage.py migrate

django-shell: migration
	$(PYTHON) usersite/manage.py shell

run: migration
	echo "Running with TAG=${TAG}"
	$(PYTHON) usersite/manage.py runserver 0.0.0.0:8000

migration-check: install
	$(PYTHON) usersite/manage.py check

# could run same command and pass table name as param
migration-update-detail: install
	$(PYTHON) usersite/manage.py sqlmigrate
	
test: migration
	$(if $(TEST_MODEL),,$(error TEST_MODEL is not defined. Please provide a value when running the command, e.g., make test TEST_MODEL=<value>))
	$(PYTHON) usersite/manage.py test tests.$(TEST_MODEL)

test-all: migration
	$(PYTHON) usersite/manage.py test tests

clean:
	$(PYENV_DEACTIVATE) && \
	pyenv uninstall $(PROJECT_NAME) && \
	rm -rf __pycache__ && \
	rm -rf .python-version && \
	echo "Cleaned up generated files"

# docker-image:
# 	docker build --progress=plain -t usersite:${VERSION} -f usersite/Dockerfile .

check_folder_not_exist:
	if [ -d "$(FOLDER_PATH)" ]; then \
		echo "Folder $(FOLDER_PATH) exists"; \
		exit 1; \
	else \
		echo "Folder $(FOLDER_PATH) does not exist"; \
		exit 0; \
	fi

create-app:
	$(if $(APP_NAME),,$(error APP_NAME is not defined. Please provide a value when running the command, e.g., make create-app APP_NAME=<value>))
	make check_folder_not_exist FOLDER_PATH=./usersite/$(APP_NAME) || exit 1
	$(PYTHON) usersite/manage.py startapp $(APP_NAME)
	mv ./$(APP_NAME) ./usersite/$(APP_NAME)

.PHONY: activate deactivate install run clean test-all test docker-image
