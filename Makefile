venv:
	python3 -m venv my_venv

update:
	./my_venv/bin/pip install -U -r requierements.txt

install: venv update

test:
	cd ./urlshortener && ../my_venv/bin/python ./manage.py test

migrate:
	cd ./urlshortener && ../my_venv/bin/python ./manage.py migrate

run:
	cd ./urlshortener && ../my_venv/bin/python ./manage.py runserver
