venv:
	python3 -m venv my_venv

yarn:
	cd ./urlshortener/shortener/static/shortener/vendor && yarn install

update:
	./my_venv/bin/pip install -U -r requierements.txt

install: venv yarn update migrate

test:
	cd ./urlshortener && ../my_venv/bin/python ./manage.py test

migrate:
	cd ./urlshortener && ../my_venv/bin/python ./manage.py migrate

run:
	cd ./urlshortener && ../my_venv/bin/python ./manage.py runserver
