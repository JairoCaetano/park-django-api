➜ django-admin startproject <project-name>
	- `django-admin` é um utilitário de comand line que fica disponível após instalar o django

- Toda pasta que tem o `__init__.py` indica que o diretório é um pacote python
- `settings.py` é uma das pastas mais importantes, ficam as configurações do Django

➜ python manage.py startapp <app-name>
	- Cria uma aplicação. Um projeto é feito de várias aplicações.
- Após criar um app, é necessário registrá-lo no `settings.py`, em `INSTALLED_APPS`

➜ python manage.py migrate
	- Cria um BD que foi configurado (sqlite3 por padrão), adicionando uma série de tabelas pré-definidas pelo Django

➜ python manage.py runserver
	- Roda a aplicação

➜ python manage.py createsuperuser
	- Para criar um admin

- VIEW
	- O Django espera que uma pasta `templates` exista, e para isso ela é manualmente criada dentro da pasta do app, onde irá armazenar os templates html da aplicação

- MODELS
	- Armazena as informações sobre os dados
	- Contém os campos e comportamentos dos dados a serem armazenados
	- Geralmente cada `model` representa uma tabela no BD

➜ python manage.py makemigrations
	- Junta tudo de novo que for criado/modificado nos models e cria dentro da pasta `migrations` um arquivo que informa o Django como a tablea deve ser montada no banco de dados

➜ python manage.py migrate
	- Irá aplicar as modificações dentro do banco de dados

---
# Questões

- WEB SERVER
- WSGI
- VIEW
	- Um trecho de código que executa o script para a página requisitada.
- MODEL
