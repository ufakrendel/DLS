import os

VOLUME_SRC = os.environ.get('VOLUME_SRC', '/home/krendel/python/DjangoDLS/')
MEDIA_SRC = os.environ.get('MEDIA_SRC', '/home/krendel/python/DjangoDLS/')
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
IS_DEBUG = bool(os.environ.get('IS_DEBUG', 'True'))