# gunicorn.conf.py

import multiprocessing

# Gunicorn configuration

# Bind to the specified IP and port
bind = '0.0.0.0:8000'

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Directory where Gunicorn should find your Django project's WSGI application
chdir = '/home/thrita/ThritaTech'

# WSGI module name
module = 'thritatech.wsgi:application'

# Enable the master process to restart workers
reload = True

# Enable graceful restarts/reloads
graceful_timeout = 30
timeout = 120
