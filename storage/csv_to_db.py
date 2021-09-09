from pandas import pandas as pd

from storage import database


class CSVToDB:
    """Base class for creating a table in the database by
        providing a model and CSV file located in the data folder."""
    def __init__(self, model):
        self.model = model
        model_name = self.model.__tablename__.lower()
        file_path = 'data/' + model_name + '.csv'
        data = pd.read_csv(file_path, header=0, delimiter=',')
        df = pd.DataFrame(data=data)
        self.records = df.to_records(index=0)
        self.session = database.connect()

    def persist_data(self):
        """Commit data an complete session after records are saved."""
        self.session.commit()  # Try to commit all the records
        self.session.close()  # Close the session
