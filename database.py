"""
Database handling code for fastloansearch using SQLAlchemy's declarative syntax
"""

__author__ = 'Doug Bromley'
__email__ = "doug@tintophat.com"

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://fls:thesparticus@localhost/fls', convert_unicode=True)
db_session = scoped_session(sessionmaker(autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """
    Initialises the database given the imported models
    """
    import models
    Base.metadata.create_all(bind=engine)