from sqlalchemy import Column, Integer, Float

from storage.database import Base


class Test(Base):
    __tablename__ = "test"
    __table_args__ = {'sqlite_autoincrement': True}
    test_id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float)
    y = Column(Float)

    @staticmethod
    def record(r):
        """Return a Test record for database records."""
        return Test(**{'x': r[0], 'y': r[1]})
