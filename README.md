# Students API (submission)

Desafio técnico de 'Empresa' desenvolvido utilizando Python, Django, Django Rest Framework, Django Filters, Python Memcached. 

A aplicação disponibiliza seis endpoints, como exigido no teste. 

## Como usar

- Instale os pacotes do requirements.txt:


Pip:
`$ pip install -r requirements.txt`

Pipenv:
`$ pipenv install -r requirements.txt`

- Crie o .env, copiando o .env_sample:
```
# Por favor, crie e altere os dados do mongoDB conforme o seu caso
$ cp .env_sample .env
```

- Importe do .csv para para o MongoDB

`$ python import_data.py`

- Crie as migrações do Django e migre as informações do database

`$ python manage.py makemigrations & python manage.py migrate`

- Instale o memcached

macOS
`$ brew install memcached`
Ubuntu 18.04
`$ sudo apt install memcached`

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

macOS
`$ memcached -vv` para visualizar os stores. 

## Documentação

A documentação está disponibilizada no path '/docs/'


