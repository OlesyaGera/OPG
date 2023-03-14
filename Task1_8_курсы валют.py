import math
Rub=int(input("Введите количество рублей для пересчета "))
K1=int(input("Введите курс евро/руб "))
K2=int(input("Введите курс долл/руб "))
x1=Rub*K1
x2=Rub*K2
print(str(Rub)+" рублей - это "+str(x1)+" евро и "+str(x2)+" долларов")