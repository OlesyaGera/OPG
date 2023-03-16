class Person():
    counter=0
    def __init__(self,name="",money=0):
        Person.counter += 1
        self.id=Person.counter
        self.name=name
        self.money =money
    def out (self):	# self - ссылка на экземпляр класса
        print("People: ",self.id, self.name,'has',self.money,'dollars.')
obj1 = Person('Bob',500)
obj2 = Person('Masha', 200)
obj1.out()
obj2.out()

