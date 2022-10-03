# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

count = int(input("Введите количество элементов списка: "))
lst = []
for i in range(count):
    lst.append(random.randint(1, 10))
print("Произвольный список:", lst)

res = []
i = 0
while i < len(lst)/2:
    res.append(lst[i] * lst[len(lst) - 1 - i])
    i += 1
if len(lst) % 2 == 1:
    res[len(res) - 1] = lst[len(lst)//2]
print("Произведение пар чисел списка:", res)
