# wisdomgroup

## 简介

智慧群团+


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

## 创建启动文件

```
vim /etc/systemd/system/wisdomgroup_uwsgi.service

[Unit]
Description=Project WisdomGroup Server
After=syslog.target

[Service]
KillSignal=SIGQUIT
ExecStart=/usr/local/python3.7/bin/uwsgi --ini /opt/production/wisdomgroup/server/uwsgi9090.ini
Restart=always
Type=notify
NotifyAccess=all
StandardError=syslog

[Install]
WantedBy=multi-user.target


systemctl enable /etc/systemd/system/wisdomgroup_uwsgi.service
systemctl start wisdomgroup_uwsgi
systemctl stop wisdomgroup_uwsgi
```

## 手工启动方式

- 启动

uwsgi --ini uwsgi9090.ini & /usr/sbin/nginx

- 关闭

cat uwsgi9090.pid|xargs kill -9