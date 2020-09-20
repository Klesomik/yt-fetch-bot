from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///../../db.sqlite'

engine = create_engine(DB_URL, connect_args={'check_same_thread': False}, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

from .channel import *

Base.metadata.create_all(engine)

session = Session()

from .api import *