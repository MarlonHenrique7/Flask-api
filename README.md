# Flask-api

Desenvolvimento de uma API de usuários utilizando o Flask. 

Rotas (endpoints) desenvolvidos:

![screencapture-localhost-5004-doc-2022-08-23-01_03_18](https://user-images.githubusercontent.com/64854811/186067204-87fc0419-9575-48fe-a83c-2ed023baa105.png)

A aplicação está configurada para ser executada em dois contaneirs do Docker, sendo um para o banco de dados e outro para a aplicação.

Comandos importantes:

Build da imagens:

```docker-compose build```

Executar os containers:

```docker-compose up -d```

Criar a database:

```docker-compose exec api python manage.py recreate_db```

Alimentar a database:

```docker-compose exec api python manage.py seed_db```

Executar os testes:

``` docker-compose exec api python -m pytest "src/tests" -p no:warnings```

Outros comandos:
```
docker-compose exec api python -m pytest "src/tests" -p no:warnings --cov="src" --cov-report html
docker-compose exec api flake8 src
docker-compose exec api black src --check
docker-compose exec api isort src --check-only
docker-compose exec api black src
docker-compose exec api isort src
```


