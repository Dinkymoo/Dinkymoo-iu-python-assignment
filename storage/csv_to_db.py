from pandas import pandas as pd

from storage.database import Database


class CSVToDB:
    """Class for creating a table in the database by
        providing a model and CSV file located in the data folder."""

    def __init__(self, model):
        self.model = model
        model_name = self.model.__tablename__.lower()
        file_path = 'data/' + model_name + '.csv'
        data = pd.read_csv(file_path, header=0, delimiter=',')
        self.session = None
        self.records = None
        self.convert_df_to_records(data)
        self.connect_to_database()
        self.persist_data()

    def convert_df_to_records(self, data):
        """Convert Pandas dataframe to a db record.
            :rtype: void """
        df = pd.DataFrame(data=data)
        self.records = df.to_records(index=0)
        if len(self.records) == 0:
            print(Exception('No records found for {}'.format(self, self.model.__tablename__)))

    def connect_to_database(self):
        """Create a database session.
            :rtype: void"""
        database = Database()
        database.connect()
        self.session = database.session
        if self.session is None:
            print(Exception('Cannot connect to DB to add'.format(self, self.model.__tablename__)))

    def persist_data(self):
        """Commit data an complete session after records are saved.
        :rtype: void
        """
        try:
            for r in self.records:
                self.session.add(self.model.record(r))
            self.session.commit()  # Try to commit all the records
            self.session.close()  # Close the session
        except Exception as error:
            print(Exception(
                'Unable to persist data record for {0}\n. {1}'.format(self, [self.model.__tablename__, error])))
