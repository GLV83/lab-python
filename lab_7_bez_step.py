from math import asin, sinh, fabs
import numpy as np
print('Вариант 7')
print('ЗАДАНИЕ. Найдите значения выражений:')
print('Y = -asin(4 * a^2 - 3 * a * x - 7 * x^2)')
print('G = 5(27 * a^2 - 51 * a * x + 20 * x^2)/-10 * a^2 + 21 * a * x + 27 * x^2)')
print('F = sinh(2 * a^2 + 21 * a * x + 10 * x^2)')
print('РЕШЕНИЕ:')

#Список для результатов
result1 = []
result2 = []
result3 = []
result = {'Y':result1, 'G':result2, 'F':result3}

while True:
    try:
        # Ввод значений
        min_x_and_a = float(input('Введите значение min:'))
        max_x_and_a = float(input('Введите значение max:'))
        if min_x_and_a >= max_x_and_a:
            print('ОШИБКА. Минимум равен или больше максимума! Введите новые значения')
            continue
        else:
            step_x_a = float(input('Введите шаг значений x и a:'))
            if step_x_a <= 0:
                print('Шаг значений x и а не может быть меньше или равен 0. Повторите ввод значений.')
                continue
            #step = int(input('Введите количество шагов вычисления функции:'))
            #if fabs((min_x_and_a - max_x_and_a) / step_x_a) <= step:
                #print('Количество шагов вычисления функции превысило максимальное значение. Повторите ввод значений, уменьшив количество шагов.')
                #continue
    except ValueError:
        print('Переключите язык. Повторите ввод значений.')
        continue

    # Автоматический подбор значений x и a
    for x in np.arange(min_x_and_a, max_x_and_a, step_x_a):
        for a in np.arange(min_x_and_a, max_x_and_a, step_x_a):

                try:
                    Y = -asin(4 * a**2 - 3 * a * x - 7 * x**2)
                    if -1 <= Y <= 1:
                        result1.append(float(round(Y,5)))
                except ValueError:
                    #print ('Значения не удовлетворяют условию Y. Введите новые значения')
                    continue
                try:
                    #G = (5 * (27 * a**2 - 51 * a * x + 20 * x**2))/(-10 * a**2 + 21 * a * x + 27 * x**2)
                    nam = 5 * (27 * a**2 - 51 * a * x + 20 * x**2)
                    nam_1 = -10 * a**2 + 21 * a * x + 27 * x**2
                    G = nam / nam_1
                    if nam_1 != 0:
                        result2.append(float(round(G,5)))
                except ZeroDivisionError:
                    #print ('Не удается найти G. На ноль делить нельзя! Введите новые значения')
                    continue
                try:
                    F = sinh(2 * a**2 + 21 * a * x + 10 * x**2)
                    if F == sinh(2 * a**2 + 21 * a * x + 10 * x**2):
                        result3.append(float(round(F,5)))
                except OverflowError:
                    #print ('Ошибка математического диапазона F. Введите новые значения')
                    continue

                else:
                    print('x = {}, a = {}, шаг = {}'.format(round(x,5), round(a,5), round(step_x_a,5)))
                    print('Y = {}'.format(Y))
                    print('G = {}'.format(G))
                    print('F = {}'.format(F))
                    print('ОТВЕТ: Y = {}, G = {}, F = {}'.format(round(Y,3),round(G,3),round(F,3)))
                    print('')
                    break

    # Цикл расчета
    #count = 0
    #while count < step:
        #np.arange(min_x_and_a, max_x_and_a, step_x_a)
        #min_x_and_a += step_x_a
        #if min_x_and_a > max_x_and_a:
            #break
        #count += 1
    break

# Запись в файл
with open('GLV_lab_7.txt', 'w') as file:
    for key, step_x_a in result.items():
        file.write('{} = {}\n' .format(key, step_x_a))

# Очистка словаря
#result = {}

# Чтение из файла
with open('GLV_lab_7.txt', 'r') as file:
    for i in file.readlines():
        key, step_x_a = i.strip().split('=')
        print(key, '=', step_x_a)

# Вывод максимального и минимального значения
    #print('Минимальные значения:  Y = {}, G = {}, F = {}'.format(min(result1),min(result2),min(result3)))
    #print('Максимальное значение: Y = {}, G = {}, F = {}'.format(max(result1),max(result2),max(result3)))
