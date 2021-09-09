from sqlalchemy import String
from sqlalchemy import Column, Integer

from storage.database import Base


class Test(Base):
    __tablename__ = "test"
    __table_args__ = {'sqlite_autoincrement': True}
    test_id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(String)
    y = Column(String)
