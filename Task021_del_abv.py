# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

txt = input("Введите текст через пробел: ")
print(f"Исходный текст: {txt}")
del_txt = "абв"
lst = [i for i in txt.split() if del_txt not in i]
print(f'Результат: {" ".join(lst)}')



