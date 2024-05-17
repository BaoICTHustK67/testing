#! /bin/bash

sleep 10
py manage.py makemigrations
py manage.py migrate