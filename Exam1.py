class CatsandDogs():
  def __init__(self, pet, breed, color, age):
     self._pet = pet
     self._breed = breed
     self._color = color
     self._age = age

  @property
  def pet(self):
    return self._pet
  
  @property
  def breed(self):
    return self._breed
  
  @property
  def color(self):
    return self._color
  
  @property 
  def age(self):
    return self._age
  
  @age.setter
  def age(self, new_age):
    if new_age > self._age:
      self._age = new_age
    return self._age
  
obj1 = CatsandDogs('Dog','York','grey',4)
print(obj1.pet)
print(obj1.breed)
print(obj1.color)
print(obj1.age)
CatsandDogs.age = 5
print(obj1.age)

input()