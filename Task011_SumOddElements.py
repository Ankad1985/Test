# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

import random

count = int(input("Введите количество элементов списка: "))
new_list = []
sum_odd_pos = 0

for i in range(count):
  new_list.append(random.randint(1,20))
  if i%2 == 0:
    sum_odd_pos+= new_list[i]
print("Полученный список:",new_list)
print("Сумма элементов на нечётных позициях:",sum_odd_pos)
  