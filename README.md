# Students API (submission)

Desafio técnico de 'Empresa' desenvolvido utilizando Python, Django, Djongo (Mongo related package) Django Rest Framework, Django Filters, Python Memcached. 

A aplicação disponibiliza seis endpoints, como exigido no teste. 

## Como usar

- Inicie o MongoDB

`brew services start mongodb-community@4.4 # macOS`

- Instale os pacotes do requirements.txt:

`$ pip install -r requirements.txt # pip`

`$ pipenv install -r requirements.txt # pipenv`

(Atenção, a biblioteca 'Djongo' tem os seguintes requirements:
* python 3.6 +
mongodb 3.6 +)

- Crie o .env, copiando o .env_sample:
```
# por favor, crie e altere os dados do mongoDB conforme o seu caso

$ cp .env_sample .env
```

- Crie uma nova SECRET_KEY:

```
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
# copiar e colar SECRET_KEY gerada no .env
```

- Importe do .csv para para o MongoDB

`$ python import_data.py`

- Crie as migrações do Django e migre as informações do database

`$ python manage.py makemigrations & python manage.py migrate`

- Instale o memcached


`$ brew install memcached # no macOS`

`$ sudo apt install memcached # no Ubuntu 18.04`

## Como testar as APIs

Este projeto está documentado com drf-yasg. Contudo, a biblioteca django_filters foi utilizada, e portanto recomenda-se o seu uso. Qual é o melhor modo?

Acesse as urls diretamente:
* /students/ - endpoint 1
* /campus/ - endpoint 2
* /students/count/ - endpoint 3
* /students/create/ - endpoint 4
* /students/search/ - endpoint 5
* /students/[ra]/[campus]/ - endpoint 6

Com exceção do endpoint 3, há um botão, do lado direito superior, chamado 'filters'. Nele, é possível acessar os parâmetros e preenchê-los conforme o desejado.

## Como testar o cache

As requests só serão armazenadas no cache do memcached caso o memcached esteja ativado. 

`$ memcached -vv # macOS # para visualizar os stores e habilitar o armazenamento em cache. ` 

## Documentação

A documentação está disponibilizada no path '/docs/'

## Misc.

Flask version: https://github.com/frnsimoes/students-api-flask