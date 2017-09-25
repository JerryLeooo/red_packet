.PHONY: clean install help test run dependencies

help:
	@echo "  clean              remove unwanted stuff"
	@echo "  install            install flaskbb and setup"
	@echo "  tests              run the testsuite"
	@echo "  run                run the development server"
	@echo "  upgrade            upgrade database of the red.instask.me"
	@echo "  ---------------------------------------------------------"

dependencies:requirements.txt
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

upgrade:
	dokku run red_packet python manage.py db upgrade

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
