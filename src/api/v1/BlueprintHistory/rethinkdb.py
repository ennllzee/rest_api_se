#!/usr/bin/sanicAPI python3
from ..rethinkdbApi import rethinkApi
from ..configure import config


class ApiRequset:
    def __init__(self):
        self.__r = rethinkApi.getR()
    
    # def getAllHistory(self, userId):
    #     cursor = self.__r.table(config.history_table).filter({'userId': userId}).without('userId').run()
    #     return [data for data in cursor]
    
    def getAllHistoryGroupTime(self, userId):
        cursor = self.__r.table(config.history_table)\
            .filter({'userId': userId})\
            .group(lambda history: history[config.create_date_key][:10])\
            .without('userId')\
            .ungroup()\
            .order_by(self.__r.desc('group'))\
            .run()
        # print([print(i) for i in cursor])
        return {group['group']: group['reduction'] for group in cursor}
    
    
    def insertHistory(self, data):
        '''
        mode:   0 is new user (open in app)
                1 is new user (register)
        '''
        data[config.create_date_key] = self.__r.now().to_iso8601()
        return self.__r.table(config.history_table).insert(data).run()
    
api = ApiRequset()