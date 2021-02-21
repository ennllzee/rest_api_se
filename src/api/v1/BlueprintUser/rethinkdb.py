#!/usr/bin/sanicAPI python3
from ..rethinkdbApi import rethinkApi
from ..configure import config

class ApiRequset:
    def __init__(self):
        self.__r = rethinkApi.getR()
    
    # def getAllQuestion(self):
    #     cursor = self.__r.table(config.question_table).run()
    #     return [data for data in cursor]
    
    # def getLimitRandomQuestion(self, limit):
    #     cursor = self.__r.table(config.question_table).sample(limit).run()
    #     return [data for data in cursor]
    '''
    mode:   0 is new user (open in app)
            1 is new user (register)
    '''
    def insertUser(self, data):
        data[config.create_date_key] = self.__r.now().to_iso8601()
        if data.get('mode', None):
            del data['mode']
            return self.__r.table(config.users_table).insert(data).run()
        else:
            return self.__r.table(config.users_table).insert(data).run()
    
api = ApiRequset()