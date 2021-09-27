from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Database:
    def __init__(self):
        self.engine = None
        self.session = None

    def connect(self):
        """Connect to database"""
        try:
            self.engine = self._create_db_engine()
            self.session = self._create_session()
        except ConnectionError:
            raise Exception('Connection error found. Unable to connect to the database engine.')
        except Exception as error:
            raise Exception('Unable to connect to the database engine. {}'.format(error))

    def _create_session(self):
        """Return a session of the created database in the db folder."""
        try:
            session = sessionmaker()
            session.configure(bind=self.engine)
            session = session()
            return session

        except Exception as error:
            raise Exception('Failed to create a database session. {}'.format(error))

    def _create_db_engine(self):
        """Create a database engine connecting to all the declarative base"""
        try:
            engine = create_engine('sqlite:///db/data.db')
            Base.metadata.create_all(engine)
            return engine

        except IOError as error:
            raise Exception(
                'Unable create a database in the db folder. Please create a db folder if it does not exist. {}'
                    .format(error))
        except Exception as error:
            raise Exception('Failed to create a database engine in the db folder. {}'.format(error))
