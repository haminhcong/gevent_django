import os, sys
# import django.core.handlers.wsgi
from gevent import wsgi
from django.core.wsgi import get_wsgi_application

import gevent.monkey

global_object = 1


def runserver():
    app_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(app_dir))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'eventlet_django.settings'
    # application = django.core.handlers.wsgi.WSGIHandler()
    application = get_wsgi_application()
    server = wsgi.WSGIServer(('', 8080), application, spawn='default')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.stop()
        sys.exit(0)


if __name__ == '__main__':
    gevent.monkey.patch_all()
    runserver()