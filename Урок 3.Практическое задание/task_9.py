"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
from random import randint

M = []
S = int(input('Задайте количество строк в матрице: '))
C = int(input('Задайте количество столбцов в матрице: '))
LST_MIN = []
for s in range(S):
    MIN = []
    for n in range(C):
        A = [randint(0, 9) for i in range(C)]
    M.append(A)
for i in range(S):
    print(M[i])
for i in range(S):
    MIN = []
    for n in range(C):
        MIN.append(M[n][i])
    LST_MIN.append(min(MIN))
print(f'{LST_MIN} минимальные значения по столбцам')
print(f'Максимальное среди них = {max(LST_MIN)}')