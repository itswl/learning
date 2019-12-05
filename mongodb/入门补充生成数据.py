import random
import json

a = {
    'name' : 'weilai',
    'age' : 18,
    'sex': 'male',
    'grade' : 45 
    }
list_json = []
for i in range(0,20):
    a['name'] = f"测试-{i}"
    a['age'] = random.randint(0, 100)
    a['sex'] =  random.choice(['male', 'female'])
    a['grade'] = random.randint(0, 100)
    j = json.dumps(a, ensure_ascii=False)
    list_json.append(j)

list_json = ','.join(list_json)
list_json = '[' + list_json +']'
print(list_json)
