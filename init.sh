#!/bin/bash

#nginx vars
nginx_path="/etc/nginx/sites-enabled"
gunicorn_path="/etc/gunicorn.d"

app_conf_path="$HOME/web/etc"


if [ -f $nginx_path/default ]; then
sudo rm /etc/nginx/sites-enabled/default
fi
sudo ln -s $app_conf_path/nginx.conf  $nginx_path/default
sudo /etc/init.d/nginx restart

sudo ln -s $app_conf_path/gunicorn.conf   $gunicorn_path/hello
sudo ln -s $app_conf_path/gunicorn_task2.conf   $gunicorn_path/django


sudo /etc/init.d/gunicorn restart
