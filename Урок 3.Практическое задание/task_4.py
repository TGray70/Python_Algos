"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint

LST = [randint(0, 5) for i in range(20)]
D = {}
for el in LST:
    A = LST.count(el)
    D.update({el: A})
K = max(D, key=D.get)
V = D[K]
print(f'В массиве {LST} чаще всего встречается число {K}, {V} раз.')
