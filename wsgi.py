#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app.configured_app()

"""
建立一个软连接
ln -s /var/www/bbs/forum.conf /etc/supervisor/conf.d/forum.conf

ln -s /var/www/bbs/forum.nginx /etc/nginx/sites-enabled/bbs



➜  ~ cat /etc/supervisor/conf.d/forum.conf

[program:bbs]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/bbs
autostart=true
autorestart=true




/usr/local/bin/gunicorn wsgi
--bind 0.0.0.0:2001
--pid /tmp/飙泪og.pid
"""
