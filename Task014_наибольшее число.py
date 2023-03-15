a = int(input('Введите число 1 -'))
b = int(input('Введите число 2 -'))
c = int(input('Введите число 3 -'))
if a < b:
    a = b
elif a < c:
    a = c

print(a)