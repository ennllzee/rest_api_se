#!/usr/bin/sanicAPI python3
from ..rethinkdbApi import rethinkApi
from ..configure import config
from collections import Counter

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
    def insert_user(self, data):
        data[config.create_date_key] = self.__r.now().to_iso8601()
        if data.get('mode', None):
            del data['mode']
            return self.__r.table(config.users_table).insert(data).run()
        else:
            return self.__r.table(config.users_table).insert(data).run()
    
    def is_correct_choice(self, choice, select_choice):
        for v in choice:
            if v.get(select_choice, None):
                return v.get(select_choice)
        return False
    
    def is_correct_choice2(self, choice, select_choice):
        return bool(list(filter(lambda x: x.get(select_choice), choice)))
    
    def get_rank(self, k, user_id):
        cursor = self.__r.table(config.history_table).eq_join('userId', self.__r.table(config.users_table)).zip()\
            .eq_join('questionId', self.__r.table(config.question_table)).run()
        rank_counter = Counter()
        for c in cursor:
            key = c['left'].get('username', c['left']['userId'])
            rank_counter[key] += self.is_correct_choice2(c['right']['choice'], c['left']['choice'])
        user_id = 13
        sorted_dict = sorted(rank_counter.items(), key=lambda x: x[1], reverse=True)
        # search key
        user_rank = -1
        for i, item in enumerate(sorted_dict):
            if item[0] == user_id:
                user_rank = i
                break
        b = user_rank != -1 and user_rank >= k
        if b:
            search_item = sorted_dict[user_rank]
            search_item = {search_item[0]: [search_item[1], user_rank+1]}
            sorted_dict = [*sorted_dict[:k], sorted_dict[user_rank]]
        else:
            sorted_dict = sorted_dict[:k]
        sorted_dict = [{item[0]: [item[1], i+1]} for i, item in enumerate(sorted_dict[:k])]
        if b: 
            sorted_dict.append(search_item)
        return sorted_dict
        
        
        
    
api = ApiRequset()