#1.	Ввести с клавиатуры два 3-значных числа и поменять у них средние цифры (например, ввести 357  и 702 – получить и вывести числа  307 и 752)
a=list(input("Число 1: "))
b=list(input("Число 2: "))
a[1]=b[1]
a1=str(int(a))
print(str(a1))


