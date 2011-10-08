import os, multiprocessing

def ensure_exists(*path):
    path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

virtualenv_dir = '/Users/justin/Sites/_virtualenvs/cobracommander'

ensure_exists(virtualenv_dir, 'logs')
ensure_exists(virtualenv_dir, 'tmp', 'pids')

name = 'gunicorn_cobracommander'
bind = '127.0.0.1:29001'
accesslog = os.path.join(ensure_exists(virtualenv_dir, 'logs'), 'gunicorn_access.log')
errorlog = os.path.join(ensure_exists(virtualenv_dir, 'logs'), 'gunicorn_errors.log')
pid = os.path.join(ensure_exists(virtualenv_dir, 'tmp', 'pids'), 'gunicorn.pid')
workers = multiprocessing.cpu_count() * 2 + 1
user = 'justin'
worker_class = 'gevent'
