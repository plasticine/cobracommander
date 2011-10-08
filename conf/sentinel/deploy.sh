#!/bin/sh

# activate virtualenv
source ../../../bin/activate

# Update requirements
pip install -r requirements.pip

# clean out unversioned files
cd ../../git clean -dfx

# activate syncdb
python ../../manage.py syncdb
python ../../manage.py migrate

# Reload the Gunicorn instance
kill -HUP `cat ../../../var/pids/gunicorn.pid`
