"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from timeit import Timer

def sn1():
    a = [0] * 100
    for i in range(100):
        a[i] = i
    a[1] = 0
    n = 2
    while n < 100:
        if a[n] != 0:
            j = n + n
            while j < 100:
                a[j] = 0
                j = j + n
        n += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    #print(b)

def sn2():
    a = [0] * 100
    for i in range(100):
        a[i] = i
    a[1] = 0
    n = 3
    b = [2]
    while n < 100:
        s = 2
        v = 1
        while (n - v) != 1:
            if a[n] % a[n - v] == 0:
                s += 1
            v += 1
        if s == 2:
            b.append(a[n])
        n += 1
    #print(b)

def sn10():
    a = [0] * 1000
    for i in range(1000):
        a[i] = i
    a[1] = 0
    n = 2
    while n < 1000:
        if a[n] != 0:
            j = n + n
            while j < 1000:
                a[j] = 0
                j = j + n
        n += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    #print(b)

def sn20():
    a = [0] * 1000
    for i in range(1000):
        a[i] = i
    a[1] = 0
    n = 3
    b = [2]
    while n < 1000:
        s = 2
        v = 1
        while (n - v) != 1:
            if a[n] % a[n - v] == 0:
                s += 1
            v += 1
        if s == 2:
            b.append(a[n])
        n += 1
    #print(b)

#sn1()
#sn2()
#sn10()
#sn20()

T1 = Timer('sn1()', 'from __main__ import sn1')
print('sn1(100)', T1.timeit(number=100), 'milliseconds')

T2 = Timer('sn2()', 'from __main__ import sn2')
print('sn2(100)', T2.timeit(number=100), 'milliseconds')

T3 = Timer('sn10()', 'from __main__ import sn10')
print('sn10(100)', T3.timeit(number=100), 'milliseconds')

T4 = Timer('sn20()', 'from __main__ import sn20')
print('sn20(100)', T4.timeit(number=100), 'milliseconds')

print('По результатам видно, что при увеличении нахождения кол-ва простых чисел, время алгоритма')
print('определения решетом растет почти линейно, а алгоритма перебором - квадратично.')
