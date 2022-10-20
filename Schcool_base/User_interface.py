def get_info():
    info = []

    last_name = input("Введите фамилию: ")
    info.append(last_name)

    first_name = input("Введите имя: ")
    info.append(first_name)

    num_class = input("Введите класс: ")
    info.append(num_class)

    perfomance = input("Введите успеваемость: ")
    info.append(perfomance)

    return info
 