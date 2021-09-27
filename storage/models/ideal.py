from sqlalchemy import Float
from sqlalchemy import Column, Integer

from storage.database import Base


class Ideal(Base):
    __tablename__ = "ideal"
    __table_args__ = {'sqlite_autoincrement': True}
    ideal_id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)
    y5 = Column(Float)
    y6 = Column(Float)
    y7 = Column(Float)
    y8 = Column(Float)
    y9 = Column(Float)
    y10 = Column(Float)
    y11 = Column(Float)
    y12 = Column(Float)
    y13 = Column(Float)
    y14 = Column(Float)
    y15 = Column(Float)
    y16 = Column(Float)
    y17 = Column(Float)
    y18 = Column(Float)
    y19 = Column(Float)
    y20 = Column(Float)
    y21 = Column(Float)
    y22 = Column(Float)
    y23 = Column(Float)
    y24 = Column(Float)
    y25 = Column(Float)
    y26 = Column(Float)
    y27 = Column(Float)
    y28 = Column(Float)
    y29 = Column(Float)
    y30 = Column(Float)
    y31 = Column(Float)
    y32 = Column(Float)
    y33 = Column(Float)
    y34 = Column(Float)
    y35 = Column(Float)
    y36 = Column(Float)
    y37 = Column(Float)
    y38 = Column(Float)
    y39 = Column(Float)
    y40 = Column(Float)
    y41 = Column(Float)
    y42 = Column(Float)
    y43 = Column(Float)
    y44 = Column(Float)
    y45 = Column(Float)
    y46 = Column(Float)
    y47 = Column(Float)
    y48 = Column(Float)
    y49 = Column(Float)
    y50 = Column(Float)

    @staticmethod
    def record(r):
        """Return a Ideal record for database records."""
        return Ideal(**{
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
