#!/usr/bin/sanicAPI python3
from ..rethinkdbApi import rethinkApi
from ..configure import config
from json import dumps

class ApiRequset:
    def __init__(self):
        self.__r = rethinkApi.getR()
        
    def getAllQuestion(self):
        cursor = self.__r.table(config.question_table).run()
        return [data for data in cursor]
    
    def getLimitRandomQuestion(self, limit):
        cursor = self.__r.table(config.question_table).sample(limit).run()
        return [data for data in cursor]
    
    def insetQuestion(self, data):
        data['create_date'] = self.__r.now().to_iso8601()
        return self.__r.table(config.question_table).insert(data).run()
    
api = ApiRequset()