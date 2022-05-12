# simpleomnichannel
simpleomnichannel

- this code created with python 3.10 and windows 10 operating sistem
- another operating sistem and/or another python version may need some adjustment

- install python 3.10
- install redis
- create new env
- activate env
- go to project folder at the same level of manage.py file
- run pip install -r requirements.txt

- run python manage.py runserver

- make sure that redis service is running(just google about it, this code use default port of redis, check it in setting.py)
- open another terminal(CMD)
- activate the same env as above
- go to project folder at the same leve of manage.py file
- run celery with command bellow
   celery -A omnichannel worker -l info -P gevent 

- for adminitrasion purpose,
- login with username admin and password a
