"""
Задача 18:
Заполнить массив случайными положительными и отрицательными целыми числами. Вывести его
на экран. Удалить из массива все отрицательные элементы и снова вывести.
"""
import numpy as np
from random import randint

np_arr = np.array([randint(-100,100) for _ in range(10)])
print("Исходный массив:", np_arr)
arr = np_arr[np_arr > 0]
print(arr)