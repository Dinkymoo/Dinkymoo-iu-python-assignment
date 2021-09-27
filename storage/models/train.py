from sqlalchemy import Column, Integer, Float

from storage.database import Base


class Train(Base):
    __tablename__ = "train"
    __table_args__ = {'sqlite_autoincrement': True}
    train_id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

    @staticmethod
    def record(r):
        """Return a Train record for database records."""
        return Train(**{'x': r[0], 'y1': r[1], 'y2': r[2], 'y3': r[3], 'y4': r[4]})
