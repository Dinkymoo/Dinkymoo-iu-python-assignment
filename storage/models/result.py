
from sqlalchemy import Column, Integer, String, Float

from storage.database import Base


class Result(Base):
    __tablename__ = "result"
    __table_args__ = {'sqlite_autoincrement': True}
    result_id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float)
    y = Column(Float)
    deltaY = Column(Float)
    noIdealFunc = Column(String)

    @staticmethod
    def record(r):
        """Return a Result record for database records."""
        return Result(**{'x': r[0], 'y': r[1], 'deltaY': r[2], 'noIdealFunc': r[3]})
