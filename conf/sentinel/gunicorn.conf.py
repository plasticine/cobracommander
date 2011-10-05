name = 'gunicorn_cobracommander'
bind = '127.0.0.1:29001'
accesslog = '/Users/justin/Sites/_virtualenvs/cobracommander/logs/gunicorn_access.log'
errorlog = '/Users/justin/Sites/_virtualenvs/cobracommander/logs/gunicorn_errors.log'
workers = 4
user = 'justin'
