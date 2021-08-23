from sqlalchemy import String, create_engine
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pandas import pandas as pd

Base = declarative_base()


class CSVToDB:
    def __init__(self, model):
        self.model = model
        model_name = self.model.__tablename__.lower()
        file_path = 'data/' + model_name + '.csv'
        engine = create_engine('sqlite:///db/data.db')
        Base.metadata.create_all(engine)
        session = sessionmaker()
        session.configure(bind=engine)
        self.session = session()
        data = pd.read_csv(file_path, header=0, delimiter=',')
        df = pd.DataFrame(data=data)
        self.records = df.to_records(index=0)


class TestToDB(CSVToDB):
    def __init__(self, model):
        super().__init__(model)

        for r in self.records:
            record = self.model(**{
                'x': r[0],
                'y': r[1]
            })
            self.session.add(record)  # Add all the records
        self.session.commit()  # Attempt to commit all the records
        self.session.close()


class TrainToDB(CSVToDB):
    def __init__(self, model):
        super().__init__(model)
        for r in self.records:
            record = model(**{
                'x': r[0],
                'y1': r[1],
                'y2': r[2],
                'y3': r[3],
                'y4': r[4]
            })
            self.session.add(record)  # Add all the records
        self.session.commit()  # Attempt to commit all the records
        self.session.close()


class IdealToDB(CSVToDB):
    def __init__(self, model):
        super().__init__(model)
        for r in self.records:
            record = model(**{
                'x': r[0],
                'y1': r[1],
                'y2': r[2],
                'y3': r[3],
                'y4': r[4],
                'y5': r[5],
                'y6': r[7],
                'y7': r[7],
                'y8': r[8],
                'y9': r[9],
                'y10': r[10],
                'y11': r[11],
                'y12': r[12],
                'y13': r[13],
                'y14': r[14],
                'y15': r[15],
                'y16': r[16],
                'y17': r[17],
                'y18': r[18],
                'y19': r[19],
                'y20': r[20],
                'y21': r[21],
                'y22': r[22],
                'y23': r[23],
                'y24': r[24],
                'y25': r[25],
                'y26': r[26],
                'y27': r[27],
                'y28': r[28],
                'y29': r[29],
                'y30': r[30],
                'y31': r[31],
                'y32': r[32],
                'y33': r[33],
                'y34': r[34],
                'y35': r[35],
                'y36': r[36],
                'y37': r[37],
                'y38': r[38],
                'y39': r[39],
                'y40': r[40],
                'y41': r[41],
                'y42': r[42],
                'y43': r[43],
                'y44': r[44],
                'y45': r[45],
                'y46': r[46],
                'y47': r[47],
                'y48': r[48],
                'y49': r[49],
                'y50': r[50]
            })
            self.session.add(record)  # Add all the records
        self.session.commit()  # Attempt to commit all the records
        self.session.close()
