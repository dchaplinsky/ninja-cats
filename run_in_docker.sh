#!/bin/bash
source /usr/local/rvm/scripts/rvm
mongod &
cd /var/task
python ./manage.py init declaration_task
python ./run.py 0.0.0.0
