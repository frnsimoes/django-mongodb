import pymongo
import pandas as pd
from decouple import config

class MongoDB(object):

    def __init__(self, database=None, collection=None):
        self.database = database
        self.collection = collection

        self.client = pymongo.MongoClient('localhost', 27017)

        self.db = self.client[self.database]

        self.col = self.db[self.collection]

    def insert_data(self, path=None):

        headers = [
            'nome', 'idade_ate_31_12_2016', 'ra', 'campus', 'municipio',
            'curso', 'modalidade', 'nivel_do_curso', 'data_inicio'
        ]

        dtypes = {
            'nome': 'str',
            'idade_ate_31_12_2016': 'str',
            'ra': 'str',
            'campus': 'str',
            'municipio': 'str',
            'curso': 'str',
            'modalidade': 'str',
            'nivel_do_curso': 'str',
            'data_inicio': 'str'
        }


        df = pd.read_csv(
            path,
            header=None,
            names=headers,
            dtype=dtypes,
            parse_dates=['data_inicio'],
            skiprows=1,
            infer_datetime_format=True,
            keep_default_na=False

            )



        data = df.to_dict('records')
        

        self.col.insert_many(data, ordered=False)




if __name__ == '__main__':
    mongodb = MongoDB(database=config('DB_NAME'),
                      collection=config('COLLECTION_NAME'))
                      
    mongodb.insert_data('dataset_estudantes.csv')

