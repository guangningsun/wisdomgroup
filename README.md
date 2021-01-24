# wisdomgroup

## 简介

智慧群团+

## 启动方式

- 启动

uwsgi --ini uwsgi9090.ini & /usr/sbin/nginx

- 关闭

cat uwsgi9090.pid|xargs kill -9


## django python3 bug修复

```
# 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
import pymysql
pymysql.install_as_MySQLdb()
```

## 创建初始用户

```
create database wisdomgroup default charset=utf8
python3 manage.py migrate
python3 manage.py makemigrations AppModel
python3 manage.py migrate AppModel

python manage.py createsuperuser
```