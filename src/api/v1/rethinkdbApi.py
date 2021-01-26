#!/usr/bin/sanicAPI python3

from rethinkdb import RethinkDB
from .configure import config

class Rethinkdb:
    def __init__(self):
        self.__r = RethinkDB()
        self.__connector = self.__r.connect(config.host, config.port, db=config.db, user=config.user, password=config.password).repl()

    async def closeDB(self):
        if self.__connector:
            self.__connector.close()
    
    def getR(self):
        return self.__r

rethinkApi = Rethinkdb()
