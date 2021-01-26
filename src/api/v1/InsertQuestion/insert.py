import os
from rethinkdb import RethinkDB

r = RethinkDB()
user = "ballyees"
password = "8cbb784f-58dc-53a7-899a-d9b133bed80a"
r.connect("localhost", 28015, user=user, password=password).repl()
question_table = r.db("daily_challenge").table('question')

def delSpace(q):
    while not q[-1]:
        del q[-1]

filename = [f for f in os.listdir() if '.txt' in f]

for d in filename:
    print(f'work on filename: {d}')
    # data = []
    with open(d, 'r', encoding='UTF-8') as file:
        question = file.read().split('#')
        del question[0]
        for q in question:
            q = q.split('\n')
            delSpace(q)
            print(q[0])
            d = {'question': q[0], 'choice': []}
            for choice in q[1:]:
                c = choice[2:]
                print(choice)
                if choice[0] == '-':
                    d['choice'].append({c: False})
                else:
                    d['choice'].append({c: True})
            d['create_date'] = r.now().to_iso8601()
            d['create_by'] = 'system'
            question_table.insert(d).run()
    # print(data)
            
        