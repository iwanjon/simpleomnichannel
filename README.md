# simpleomnichannel
simpleomnichannel
######################################
- this code created with python 3.10 and windows 10 operating sistem
- another operating sistem and/or another python version may need some adjustment

######################################
######################################
- install python 3.10
- install redis
- create new env
- activate env
- go to project folder at the same level of manage.py file
- run pip install -r requirements.txt

######################################
######################################
- run python manage.py makemigrations
- run python manage.py migrate
- create superuser (python manage.py createsuperuser) run in terminal at thesame level as manage.py
- run python manage.py runserver

######################################
######################################
- for using example data:
- create 4 number channel first, because channel need 4 channel to be run successfully, go to menu channel to create channel.
- create media folder in the same level as manage.py
- exmaple data in folder contoh data
######################################
######################################
- make sure that redis service is running(just google about it, this code use default port of redis, check it in setting.py)
- open another terminal(CMD)
- activate the same env as above
- go to project folder at the same leve of manage.py file
- run celery with command bellow
- celery -A omnichannel worker -l info -P gevent 

