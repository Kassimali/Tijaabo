import json

person='{"Name":"Kassim Mohamed","Country":"Somalia","City":"Mogadishu","Languages":["English","Arabic"]}'

person_dic=json.loads(person)

print(person_dic)

print(person_dic['languages'])