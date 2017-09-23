.PHONY: clean install help test run dependencies

help:
	@echo "  clean              remove unwanted stuff"
	@echo "  install            install flaskbb and setup"
	@echo "  tests              run the testsuite"
	@echo "  run                run the development server"
	@echo "  deploy             deploy to www.instask.me"
	@echo "  upgrade            upgrade database of the www.instask.me"
	@echo "  ---------------------------------------------------------"
	@echo "  deploy to test     fab deploy_test:branch=branch_name"

dependencies:requirements.txt
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

upgrade:
	dokku run instask python manage.py db upgrade

export:
	dokku postgres:export instask-database > /tmp/instask.dump

import:
	dokku postgres:import instask-test-database < /tmp/instask.dump

migrate_test:
	./bin/migration.sh

unittest:
	py.test --cov=red_packet --cov-report=term-missing tests/unittests -vv

apitest:
	py.test --cov=red_packet --cov-report=term-missing tests/apitests -vv

test:
	py.test --cov=red_packet --cov-report=term-missing tests -vv

run:
	python manage.py runserver -dr

install:dependencies
	clear
	python manage.py install

routes:
	python manage.py list_routes

doc:
	bootprint openapi docs/swagger.yaml docs
