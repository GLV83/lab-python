from math import asin, sinh
print('Вариант 7')
print('ЗАДАНИЕ. Найдите значения выражений:')
print ('G = 5(27 * a^2 - 51 * a * x + 20 * x^2)/-10 * a^2 + 21 * a * x + 27 * x^2)')
print ('F = sinh(2 * a^2 + 21 * a * x + 10 * x^2)')
print ('Y = -asin(4 * a^2 - 3 * a * x - 7 * x^2)')
print('РЕШЕНИЕ:')
import numpy as np
while True:
    min_x_and_a = float(input('Введите значение min:'))
    max_x_and_a = float(input('Введите значение max:'))
    if min_x_and_a >= max_x_and_a:
        print('ОШИБКА. Минимум равен или больше максимума! Введите новые значения')
        continue
    else:
        step_x_a = float(input('Введите шаг значений x и a:'))
    for x in np.arange(min_x_and_a, max_x_and_a, step_x_a):
        for a in np.arange(min_x_and_a, max_x_and_a, step_x_a):
            try:
                #G = (5 * (27 * a**2 - 51 * a * x + 20 * x**2))/(-10 * a**2 + 21 * a * x + 27 * x**2)
                nam = 5 * (27 * a**2 - 51 * a * x + 20 * x**2)
                nam_1 = -10 * a**2 + 21 * a * x + 27 * x**2
                G = nam / nam_1
                F = sinh(2 * a**2 + 21 * a * x + 10 * x**2)
                Y = -asin(4 * a**2 - 3 * a * x - 7 * x**2)
                if -1 <= Y <= 1:
                    continue
            except ValueError:
                #print ('Значения не удовлетворяют условию Y. Введите новые значения')
                continue
            except ZeroDivisionError:
                #print ('Не удается найти G. На ноль делить нельзя! Введите новые значения')
                break
            except OverflowError:
                #print ('Ошибка математического диапазона F. Введите новые значения')
                break
            else:
                print('x = {} , a = {}, шаг = {}'.format(round(x,5), round(a,5), round(step_x_a,5)))
                print ('Y = {}'.format(Y))
                print ('G = {}'.format(G))
                print ('F = {}'.format(F))
                print('ОТВЕТ: G = {} , F = {} , Y = {}'.format(round(G,3),round(F,3),round(Y,3)))
                print ('')
    break
