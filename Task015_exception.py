# Исключения

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("деление на ноль")
    except TypeError:
        print("ошибка ввода типа данных")
    except:
        print("остальные ошибки")
    else:
        print("результат ок", result)
    finally:
        print("выполнение функции закончено")


def correctDigitInput():
    while True:
        try:
            x = int(input("Введите число: "))
            break
        except ValueError:
            print("это не число! введите число")
    return x

a = correctDigitInput()
b = correctDigitInput()

divide(a,b)

print("Программа продолжается ...")