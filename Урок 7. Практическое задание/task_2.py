"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random

def mergeSort(lst):
    if len(lst)>1:
        mid = len(lst)//2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                lst[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            lst[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            lst[k]=righthalf[j]
            j=j+1
            k=k+1
    return lst

n = int(input('Введите число элементов: '))
LST = [random.uniform(0, 50) for i in range(0,n)]
print(f'Исходный - {LST}')
N_LST = mergeSort(LST)
print(f'Отсортированный - {N_LST}')











