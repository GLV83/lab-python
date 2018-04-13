from math import asin, sinh
import numpy as np
print('Вариант 7')
# Формулировка задания
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
    # Ввод значений
    min_x_and_a = float(input('Введите значение min:'))
    max_x_and_a = float(input('Введите значение max:'))
    if min_x_and_a >= max_x_and_a:
        print('ОШИБКА. Минимум равен или больше максимума! Введите новые значения')
        continue
    else:
        step_x_a = float(input('Введите шаг значений x и a:'))

        # Автоматический подбор значений x и a
        for x in np.arange(min_x_and_a, max_x_and_a, step_x_a):
            for a in np.arange(min_x_and_a, max_x_and_a, step_x_a):

                # Вычистение значений функций, обработка исключений и запись результатов в списки
                try:
                    Y = -asin(4 * a**2 - 3 * a * x - 7 * x**2)
                    if -1 <= Y <= 1:
                        result1.append(float(round(Y,5)))
                except ValueError:
                    #print ('Значения не удовлетворяют условию Y. Введите новые значения')
                    break

                try:
                    #G = (5 * (27 * a**2 - 51 * a * x + 20 * x**2))/(-10 * a**2 + 21 * a * x + 27 * x**2)
                    nam = 5 * (27 * a**2 - 51 * a * x + 20 * x**2)
                    nam_1 = -10 * a**2 + 21 * a * x + 27 * x**2
                    G = nam / nam_1
                    if nam_1 != 0:
                        result2.append(float(round(G,5)))
                except ZeroDivisionError:
                    #print ('Не удается найти G. На ноль делить нельзя! Введите новые значения')
                    break
                try:
                    F = sinh(2 * a**2 + 21 * a * x + 10 * x**2)
                    if F == sinh(2 * a**2 + 21 * a * x + 10 * x**2):
                        result3.append(float(round(F,5)))
                except OverflowError:
                    #print ('Ошибка математического диапазона F. Введите новые значения')
                    break

                #else:
                    # Вывод на экран результатов вычислений
                    #print('x = {}, a = {}, шаг = {}'.format(round(x,5), round(a,5), round(step_x_a,5)))
                    #print('Y = {}'.format(Y))
                    #print('G = {}'.format(G))
                    #print('F = {}'.format(F))
                    #print('ОТВЕТ: Y = {}, G = {}, F = {}'.format(round(Y,3),round(G,3),round(F,3)))
                    #print(' ')
                    #continue
    break

# Запись в файл

file = open('lab_7_1.txt', 'w')
file.write('Y = {}\n'.format(result1))
file.write('G = {}\n'.format(result2))
file.write('F = {}\n'.format(result3))
file.close()

# Чтение из файла
with open('lab_7_1.txt', 'r') as file:
    for result1 in file.readlines():
        Y = result1
        print(Y.format(result1))
    for result2 in file.readlines():
        G = result2
        print(G.format(result2))
    for result3 in file.readlines():
        F = result3
        print(F.format(result3))
