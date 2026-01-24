import os 
import sys
import json
import certifi

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.my_logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkSecurityDataPush:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) 

    def cv_to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            record = list(json.loads(df.T.to_json()).values())
            return record
        except Exception as e:  
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL, tls=True,
    tlsCAFile=certifi.where())
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)

            return(len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ =='__main__':
    FILE_PATH='Network_data\phisingData.csv'
    DATABASE='AFFANAI'
    Collection="NetworkData"

    networkobj=NetworkSecurityDataPush()
    records=networkobj.cv_to_json(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)



