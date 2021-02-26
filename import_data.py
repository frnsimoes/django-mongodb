from pymongo import MongoClient
import csv
client = MongoClient('localhost', 27017)
db = client["rlaura"]
col = db["core_students"]
with open('dataset_estudantes.csv', 'r') as read_obj:
    csv_reader = csv.DictReader(read_obj)
    mylist = list(csv_reader)
    x = col.insert_many(mylist)

