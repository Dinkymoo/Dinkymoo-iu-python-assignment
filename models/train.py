from sqlalchemy import String
from sqlalchemy import Column, Integer, Float, Date
from db_orm_models import Base


class Train(Base):
    __tablename__ = "train"
    __table_args__ = {'sqlite_autoincrement': True}
    train_id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(String)
    y1 = Column(String)
    y2 = Column(String)
    y3 = Column(String)
    y4 = Column(String)
