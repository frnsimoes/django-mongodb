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



# Maiores desafios

- import_data.py e modelagem MongoDB

Como eu nunca havia utilizado pandas e não tinha nenhuma experiência com MongoDB, tudo foi muito novo para mim.

Passei um bom tempo tentando fazer o download do Mongo, até achavar um vídeo do traversy media. No macOS, a coisa foi simplificada com o `brew`. 

Depois, obviamente, a questão foi importar todos os dados para o DB. Minha primeira tentativa foi com um simples script de leitura de arquivo. Deu certo, mas foi uma confusão. Salvei todos os dados na forma de um único documento. Não era o que eu queria, então busquei alternativas no stackoverflow, lembrando então da alternativa de usar o pandas.

- Problemas de modelagem

O maior problema, que resolvi postergar, inclusive, por julgar que não haveria tempo, foi responder a questão: Ok, o MongoDB é diferente de Postgresql em basicamente tudo, mas eu tenho certeza de que é possível fazer as collections interagirem assim como as tabelas se interagem no SQL. 

Pesquisando, descobri que seria possível 'linká-las', mas não fui a fundo. Confesso que fiquei com medo de perder muito tempo manipulando o `import_data.py` para adequar as collections ao que eu imaginava que seria o correto fazer. 

- Problemas com o pandas

Nenhuma muito grande, mas foram pequenos desafios: descobrir como passar string para date type, e descobrir como retirar o '.0' dos números de RA (para utilizá-los nas urls) o replace, utilizando regex.

- Cache

Esta também foi uma oportunidade para aprender sobre cache, assunto que eu sempre quis começar a estudar. Aprendi o básico do básico, mas consegui entender a utilidade de utilizá-lo num banco de dados com muitas entradas. 

# Acertos

A parte 2 do desafio foi bem interessante. Aprendi maiores detalhes sobre o django-filters, aprendi mais sobre o código base do django rest framework, e aprendi a ser mais criterioso no uso de ConcreteViews e APIViews. Esta também foi uma boa oportunidade para entender o papel dos comentários de classe e documentação. 

# Misc

Gostaria de ter tido mais tempo para aprender desenvolver o projeto em Flask. Comecei o começo-do-começo, mas foi apenas isso. 

