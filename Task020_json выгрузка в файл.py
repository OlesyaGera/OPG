import json
data = {"id":765,"email":"ivanov@mail.ru","surname":"Иванов","age":45,"admin":False,"friends":[123,456,789]}
# преобразуем словарь в json и записываем в файл
with open('data.json','w',encoding='UTF-8') as file:
    json.dump(data,file)
# преобразуем словарь в json и записываем в файл
with open('data.json','w',encoding='UTF-8') as file:
    json.dump(data,file,ensure_ascii=False)

