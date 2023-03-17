import random
import time

def welcoming():
    print("Добро пожаловать в нашу ветклинику!")
    print()

def pet():
    pet=0
    while pet!=1 and pet!=2:
        print("Кого будем лечить? Кошечку (нажмите 1) или собачечку (нажмите 2)?")
        pet=int(input())
    return pet

def check(chosenpet):
    print(' Проверяем возможность...')
    time.sleep(2)

    friendlypet = random.randint(1, 2)

    if chosenpet == friendlypet:
        print('О, да! Рады вас видеть')
    else:
        print('Ой, извините. но блохастиков мы сегодня не лечим!')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    welcoming()
    petNumber = pet()
    check(petNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()
