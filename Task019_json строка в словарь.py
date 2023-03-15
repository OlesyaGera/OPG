import json
string='{"id":765,"email":"ivanov@mail.ru","surname":"Иванов","age":45,"admin":false,"friends":[123,456,789]}'
data=json.loads(string)
print(data["email"])
print(data["surname"])
print(data["admin"])
print(data["friends"])
