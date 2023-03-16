# Создание класса
class Person():
    counter=0
    def __new__(cls, *args,**kwargs):
        print("вызов __new__ для ",str(cls))
        return super().__new__(cls)

    def __init__(self,name="",money=0) -> None:
        Person.counter += 1
        self.id=Person.counter
        self.name=name
        self.money=money
        print("Создан ",self.__str__())

    def out (self):	# self - ссылка на экземпляр класса
        print("People: ",self.name,'has',self.money,'dollars.')

    def changename (self,newname):
        self.name = newname
        self.out()

    def changemoney (self,newmoney):
        self.money = newmoney
        print(self.__str__())

    def __str__(self):
        return "Пользователь: "+self.name+' с '+str(self.money)+' рублями.'

p1=Person()