import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab
import time

plt.axis('equal')   # масштаб осей Х и У одинаковый (чтобы круг не был овалом)

# задаем центр окружности
r = float(input('Введите значение радиуса:'))
centr_x = float(input('Введите значение x для центра окружности:'))
centr_y = float(input('Введите значение y для центра окружности:'))
# задаем множество точек координатной плоскости
N = int(input('Введите количество точек на плоскости:'))
result = []
start = time.time()
times = []
for i, _ in enumerate(range(N)):
    x = pylab.randint(-10,10)
    y = pylab.randint(-10,10)
    np.append(x, y)
    plt.scatter(x, y, color='black')
    # опредиляем количество точек, лежащих в окружности
    if ((centr_x**2) + (centr_y**2)) == r**2:
        result.append(format([x, y]))
        #print('Точка является центром окружности', (x,y))

    elif ((x-centr_x)**2) + ((y - centr_y)**2) == r**2:
        result.append(format([x, y]))
        #print('Точка лежит на окружности', (x,y))

    elif ((x-centr_x)**2) + ((y - centr_y)**2) < r**2:
        result.append(format([x, y]))
        #print('Точка входит в окружность',(x,y))

# рисуем центр окружности, окружность
plt.scatter(centr_x, centr_y)
circul = plt.Circle((centr_x, centr_y), r, facecolor='none', edgecolor='red')
plt.gca().add_artist(circul)
plt.show()

# Считаем количество точек, принадлежащих окружности
#print(result)

new_result = set(result)
print('Результат:', new_result)
L = len(new_result)
print('Количество точек принадлежащих окружности', L)
end = time.time()
times.append(end - start)
print('Время выполнения поиска точек:', *times)

# Запись в файл времени выполнения
times = str(times)
file = open('time.txt', 'w')
file.write(times)
file.close()
print('Время выполнения записано в файл time.txt')
