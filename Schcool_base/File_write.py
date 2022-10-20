from User_interface import get_info as g

info = g()

def writing_scv():
    with open("School_base.csv", "a", encoding="utf-8") as file:
        file.write(
            f"Фамилия: {info[0]}\nИмя: {info[1]}\nКласс: {info[2]}\nУспеваемость: {info[3]}\n\n"
        )


