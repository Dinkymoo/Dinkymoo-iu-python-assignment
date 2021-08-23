from db_orm_models import TestToDB, TrainToDB, IdealToDB
from models.ideal import Ideal
from models.test import Test
from models.train import Train

TestToDB(Test)
TrainToDB(Train)
IdealToDB(Ideal)

