from storage.csv_to_db import CSVToDB
from storage.models.ideal import Ideal
from storage.models.result import Result
from storage.models.test import Test
from storage.models.train import Train


CSVToDB(Test)
CSVToDB(Train)
CSVToDB(Ideal)
CSVToDB(Result)
