# Virtual Environment

python3 -m venv venv
source venv/bin/activate

# Installs

pip install django
pip install celery
pip install redis
pip install beautifulsoup4
pip install selenium

pip freeze > requirements.txt

# Docker

chmod +x docker-entrypoint.sh

docker-compose up -d --build

# Django

django-admin startproject mysite

```

```
