import sys
from os import environ

DB_URL = 'sqlite:///../db.sqlite'

if 'TG_TOKEN' not in environ:
    sys.exit(1)

TG_TOKEN = environ['TG_TOKEN']