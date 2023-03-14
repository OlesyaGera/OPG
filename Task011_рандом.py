# import random
from random import shuffle
from random import randint
import array
N=int(input())
A=[randint(1,N) for x in range (N)]
print("Тип данных ", type(A))
shuffle(A)
print(A)
