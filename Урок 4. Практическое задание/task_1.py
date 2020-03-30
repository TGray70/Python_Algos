"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from random import randint
from timeit import Timer

def cal1():
    n = randint(10, 19)
    s = 0
    while s < len(str(n)):
        even = 0
        not_ev = 0
        for i in str(n):
            i = int(i)
            if (i % 2) == 0:
                even += 1
            else:
                not_ev += 1
        S = even + not_ev
        s += 1
    #print(f'В числе {n} {S} цифры, четныхх - {EVEN}, не четных - {NOT_EV}')

def cal2():
    number = randint(10, 19)
    even = 0
    not_ev = 0
    i = 0
    n = len(str(number))
    while i < n:
        с = number % 10**(n) // 10**(n-1)
        if (с % 2) == 0:
            even += 1
        else:
            not_ev += 1
        n -= 1
    S = even + not_ev
    #print(f'В числе {NUMBER} {S} цифры, четных - {EVEN}, не четных - {NOT_EV}')

#cal1()
#cal2()

T1 = Timer('cal1()', 'from __main__ import cal1')
print('cal1(10000)', T1.timeit(number=10000), 'milliseconds')

T2 = Timer('cal2()', 'from __main__ import cal2')
print('cal2(10000)', T2.timeit(number=10000), 'milliseconds')

T3 = Timer('cal1()', 'from __main__ import cal1')
print('cal1(100000)', T3.timeit(number=1000000), 'milliseconds')

T4 = Timer('cal2()', 'from __main__ import cal2')
print('cal2(100000)', T4.timeit(number=1000000), 'milliseconds')

print('По результатам видно, что получать цифры из числа быстрее вычеслениями,')
print('чем переводить в строку, а потом обратно.')
print('Время, при увеличении циклов, растет линейно в обоих алгоритмах')
print()
def in1():
    a = []
    for i in range(10):
        a.append(i)

def in2():
    a = [0] * 10
    for i in range(10):
        a[i] = i

T5 = Timer('in1()', 'from __main__ import in1')
print('in1(10000)', T5.timeit(number=10000), 'milliseconds')

T6 = Timer('in2()', 'from __main__ import in2')
print('in2(10000)', T6.timeit(number=10000), 'milliseconds')

T7 = Timer('in1()', 'from __main__ import in1')
print('in1(100000)', T7.timeit(number=1000000), 'milliseconds')

T8 = Timer('in2()', 'from __main__ import in2')
print('in2(100000)', T8.timeit(number=1000000), 'milliseconds')

print('По результатам видно, что заполнение предварительно созданного нулевого списка')
print('нужного размера быстрее, чем заполнение предварительно созданного пустого списка.')
print('Время, при увеличении циклов, растет линейно в обоих алгоритмах')
