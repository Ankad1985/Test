# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
#[15, 16, 2, 3, 1, 7, 5, 4, 10]
#[16, 3, 7, 10]

#lst = [int(i) for i in input("Введите список чисел: ").split()]
lst = [15, 16, 2, 3, 1, 7, 5, 4, 10]
new_lst = [lst[i] for i in range(1,len(lst)) if lst[i] > lst[i-1]]
print(new_lst)