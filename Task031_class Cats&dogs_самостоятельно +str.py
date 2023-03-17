class Cats_and_dogs:
    def __init__(self, person, pet, pet_name):
        self.person = person
        self.pet = pet
        self.pet_name = pet_name
        print(self.person," has a ",self.pet, ". Her name is ", self.pet_name)
    def __str__(self):
        return(self.person+self.pet,+self.pet_name)
obj1 = Cats_and_dogs("Juliana","dog","Sosiska")
