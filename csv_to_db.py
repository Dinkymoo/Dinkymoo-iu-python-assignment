from storage.db_orm_models import TestToDB, TrainToDB, IdealToDB
from storage.models.ideal import Ideal
from storage.models.test import Test
from storage.models.train import Train


TestToDB(Test)
TrainToDB(Train)
IdealToDB(Ideal)

