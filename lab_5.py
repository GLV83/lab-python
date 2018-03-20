from math import asin, sinh
import numpy as np
print('Вариант 7')
print('ЗАДАНИЕ. Найдите значения выражений:')
print('Y = -asin(4 * a^2 - 3 * a * x - 7 * x^2)')
print('G = 5(27 * a^2 - 51 * a * x + 20 * x^2)/-10 * a^2 + 21 * a * x + 27 * x^2)')
print('F = sinh(2 * a^2 + 21 * a * x + 10 * x^2)')
print('РЕШЕНИЕ:')
# Список для результатов
result = []

while True:
    min_x_and_a = float(input('Введите значение min:'))
    max_x_and_a = float(input('Введите значение max:'))
    if min_x_and_a >= max_x_and_a:
        print('ОШИБКА. Минимум равен или больше максимума! Введите новые значения')
        continue
    else:
        step_x_a = float(input('Введите шаг значений x и a:'))
        #step = int(input('Введите количество шагов вычисления функции: '))
        choose = int(input('1 - функция Y\n2 - функция G\n3 - функция F\nВыберите функцию: '))

    for x in np.arange(min_x_and_a, max_x_and_a, step_x_a):
        for a in np.arange(min_x_and_a, max_x_and_a, step_x_a):
            if choose == 1:
                try:
                    Y = -asin(4 * a**2 - 3 * a * x - 7 * x**2)
                    if -1 <= Y <= 1:
                        print('x = {}, a = {}, шаг = {}'.format(round(x,5), round(a,5), round(step_x_a,5)))
                        print('Y = {}'.format(Y))
                        result.append(float(round(Y,5)))
                except ValueError:
                    # print ('Значения не удовлетворяют условию Y. Введите новые значения')
                    continue
            if choose == 2:
                try:
                    # G = (5 * (27 * a**2 - 51 * a * x + 20 * x**2))/(-10 * a**2 + 21 * a * x + 27 * x**2)
                    nam = 5 * (27 * a**2 - 51 * a * x + 20 * x**2)
                    nam_1 = -10 * a**2 + 21 * a * x + 27 * x**2
                    G = nam / nam_1
                    if nam_1 != 0:
                        print('x = {}, a = {}, шаг = {}'.format(round(x,5), round(a,5), round(step_x_a,5)))
                        print('G = {}'.format(G))
                        result.append(float(round(G,5)))
                except ZeroDivisionError:
                    # print ('Не удается найти G. На ноль делить нельзя! Введите новые значения')
                    continue
            if choose == 3:
                try:
                    F = sinh(2 * a**2 + 21 * a * x + 10 * x**2)
                    if F == sinh(2 * a**2 + 21 * a * x + 10 * x**2):
                        print('x = {}, a = {}, шаг = {}'.format(round(x,5), round(a,5), round(step_x_a,5)))
                        print('F = {}'.format(F))
                        result.append(float(round(F,5)))
                except OverflowError:
                    # print ('Ошибка математического диапазона F. Введите новые значения')
                    continue
    # Результаты
    for key in result:
        print(result)
    break
# Вывод максимального и минимального значения
print('Минимальные значения: ', min(result))
print('Максимальное значение: ', max(result))
