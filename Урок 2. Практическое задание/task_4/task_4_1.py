"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
try:
    N = int(input('Введите число елементов в последовательности: '))
    S = 1
    i = 1
    El = 1
    while i < N:
        El /= -2
        S = S + El
        i += 1
    print(f'Кол-во элементов: {N}, их сумма: {S}')
except ValueError:
    print('Вы ввели не число, повторите.')



