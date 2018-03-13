from math import asin, sinh
print('Вариант 7')
print('ЗАДАНИЕ. Найдите значения выражений:')
print ('G = 5(27 * a^2 - 51 * a * x + 20 * x^2)/-10 * a^2 + 21 * a * x + 27 * x^2)')
print ('F = sinh(2 * a^2 + 21 * a * x + 10 * x^2)')
print ('Y = -asin(4 * a^2 - 3 * a * x - 7 * x^2)')
print('РЕШЕНИЕ:')
while True:
    x = float(input('Введите значение x:'))
    a = float(input('Введите значение a:'))
    try:
       #G = (5 * (27 * a**2 - 51 * a * x + 20 * x**2))/(-10 * a**2 + 21 * a * x + 27 * x**2)
        nam = 5 * (27 * a**2 - 51 * a * x + 20 * x**2)
        nam_1 = -10 * a**2 + 21 * a * x + 27 * x**2
        G = nam / nam_1
        F = sinh(2 * a**2 + 21 * a * x + 10 * x**2)
        Y = -asin(4 * a**2 - 3 * a * x - 7 * x**2)
        if -1 <= Y <= 1:
            print(' ')
    except ValueError:
        print ('Значения не удовлетворяют условию Y. Введите новые значения')
        continue
        if nam_1 != 0:
            print(' ')
    except ZeroDivisionError:
        print ('Не удается найти G. На ноль делить нельзя! Введите новые значения')
        continue
    except OverflowError:
        print ('Ошибка математического диапазона F. Введите новые значения')
        continue
    else:
        print ('Y = {}'.format(Y))
        print ('G = {}'.format(G))
        print ('F = {}'.format(F))
        print('ОТВЕТ: G = {} , F = {} , Y = {}'.format(round(G,5),round(F,5),round(Y,5)))
        break
