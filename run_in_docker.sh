#!/bin/bash
source /usr/local/rvm/scripts/rvm
mongod &
cd /var/task
./manage.py init declaration_task
./run.py
