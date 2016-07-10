import logging
import threading

from sqlalchemy import engine_from_config, event, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.schema import MetaData
from sqlalchemy import pool
from zope.sqlalchemy import ZopeTransactionExtension

metadata = MetaData(naming_convention={
    "ix": '%(table_name)s_%(column_0_name)s_idx',
    "uq": "%(table_name)s_%(column_0_name)s_uk",
    "ck": "%(table_name)s_%(constraint_name)s_ck",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey"
})

_SESSION_LOCK = threading.Lock()
_SESSION = None

Base = declarative_base(metadata=metadata)


def create_database_session(settings,
                            request_scoped=False,
                            prefix='sqlalchemy.'):

    engine = engine_from_config(settings, prefix=prefix)
    if request_scoped:
        maker = sessionmaker(bind=engine, extension=ZopeTransactionExtension())
    else:
        maker = sessionmaker(bind=engine)

    session = scoped_session(maker)
    event.listen(session, 'after_begin', set_timezone)
    return session


def set_timezone(session, transaction, connection):
   """Sets the timezone to EST5EDT."""
   session.execute("set timezone = 'EST5EDT'")
