class Cats_and_dogs:
    def __init__(self, person, pet, pet_name):
        self.person = person
        self.pet = pet
        self.pet_name = pet_name
    def out (self):
        print(self.person," has a ",self.pet, ". Her name is ", self.pet_name)
    def changepet_name (self, newpet_name):
        self.pet_name=newpet_name
obj1 = Cats_and_dogs("Juliana","dog","Sosiska")
obj1.out()
obj1.changepet_name("Kolbaska")
obj1.out()