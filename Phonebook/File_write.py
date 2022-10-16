from User_interface import get_info as g
import json

info = g()


def writing_scv():
    with open("Phonebook.csv", "a", encoding="utf-8") as file:
        file.write(
            f"Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n"
        )


def writing_json():
    with open("Phonebook.json", "w") as file:
        json.dump(info, file, indent=2, ensure_ascii=False)
