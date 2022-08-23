# Flask-api

Desenvolvimento de uma API de usuários utilizando o Flask. 

Rotas (endpoints) desenvolvidos:

![screencapture-localhost-5004-doc-2022-08-23-01_03_18](https://user-images.githubusercontent.com/64854811/186067204-87fc0419-9575-48fe-a83c-2ed023baa105.png)

A aplicação está configurada para ser executada em dois contaneirs do Docker, sendo um para o banco de dados e outro para a aplicação.

Comandos importantes:

Build da imagens:

`
$ docker-compose build

`


Run the containers:

$ docker-compose up -d
Create the database:

$ docker-compose exec api python manage.py recreate_db
Seed the database:

$ docker-compose exec api python manage.py seed_db
Run the tests:

$ docker-compose exec api python -m pytest "src/tests" -p no:warnings
Run the tests with coverage:

$ docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src"
Run the tests with coverage and generate an HTML report of the results:

$ docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src" --cov-report html
Lint:

$ docker-compose exec api flake8 src
Run Black and isort with check options:

$ docker-compose exec api black src --check
$ docker-compose exec api isort src --check-only
Make code changes with Black and isort:

$ docker-compose exec api black src
$ docker-compose exec api isort src


