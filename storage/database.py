from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def connect():
    """Return a session of the created database engine."""
    engine = create_engine('sqlite:///db/data.db')
    Base.metadata.create_all(engine)
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    return session

