# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random
from random import randint
lens_n = int(input("Введите количество элементов первого множества n: "))
numbers_n = []
for i in range(lens_n):
    numbers_n.append(randint(0, 10))
print(numbers_n)
lens_m = int(input("Введите количество элементов второго множества m: "))
numbers_m = []
for i in range(lens_m):
    numbers_m.append(randint(0, 10))
print(numbers_m)
lens_all = list(set(numbers_n) & set(numbers_m))
lens_all.sort()
print(f"Числа, встречающиеся в обоих элементах: {lens_all}")