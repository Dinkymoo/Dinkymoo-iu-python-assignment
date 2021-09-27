import unittest

from storage.database import Database
from storage.csv_to_db import convert_df_to_records,connect_to_database,persist_data
from unittest.mock import MagicMock


class TestCSVToDBMethods(unittest.TestCase):

    def test_database_connection(self):
        """Return database session"""

        database = Database()
        database._create_db_engine = MagicMock(return_value='engine')
        database._create_session = MagicMock(return_value='session')
        database.connect()
        self.assertEqual(database.session, 'session')

    def test_database_create_engine(self):
        """Return database engine"""

        database = Database()
        database._create_engine = MagicMock(return_value='engine')
        database._create_session = MagicMock(return_value='session')
        database.connect()
        self.assertEquals(database.engine, 'engine')

    def test_database_throw_IOException(self):
        """Return exception in case IOError"""

        database = Database()
        database._create_db_engine = MagicMock(return_value=IOError)
        database._create_session = MagicMock(return_value=ValueError)
        database.connect()
        self.assertRaises(Exception)

    def test_database_throw_exception(self):
        """Return exception in case Exception"""

        database = Database()
        database._create_db_engine = MagicMock(return_value=Exception)
        database._create_session = MagicMock(return_value='session')
        database.connect()
        self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()
