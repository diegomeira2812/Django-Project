# Task Manager - Django

Sistema web de gerenciamento de tarefas desenvolvido com Django, com autenticação de usuários e operações completas de CRUD.

## Funcionalidades

- Cadastro de usuários (via Django Auth)
- Login e logout
- Criação de tarefas
- Listagem de tarefas
- Edição de tarefas
- Exclusão de tarefas
- Marcar tarefas como concluídas
- Cada usuário visualiza apenas suas próprias tarefas

## Tecnologias utilizadas

- Python
- Django
- SQLite

## Como executar o projeto

### 1. Clonar repositório

git clone https://github.com/diegomeira2812/Django-Project.git

### 2. Criar ambiente virtual

python -m venv venv  
venv\Scripts\activate 

### 3. Instalar dependências

pip install django

### 4. Rodar migrations

python manage.py makemigrations  
python manage.py migrate 

### 5. Criar superusuario

python manage.py createsuperuser

### 6. Rodar servidor

python manage.py runserver


