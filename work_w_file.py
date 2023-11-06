import csv
import datetime
import pandas as pd
import re


def choose(choice):
    if choice == 'add':
        return add_info()
    elif choice == "read":
        return read_info()
    elif choice == "edit":
        return edit_info()
    elif choice == "delete":
        return delete_info()

    elif choice == "stop":
        exit()
    else:
        return choose(input('Неверная команда. Введите add, read, edit, delete или stop: '))


def get_max_index():
    df = pd.read_csv('data.csv', delimiter=";")
    if df.shape[0] == 0:
        return 0
    max_index = df['Index'].max()
    return max_index


def add_info():
    index_id = get_max_index() + 1
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    with open("data.csv", "a", encoding="utf-8") as file:
        names = ["Index", "Title", "Body", "Date"]
        file_writer = csv.DictWriter(file, delimiter=";",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writerow(
            {"Index": index_id, "Title": title, "Body": body, "Date": datetime.datetime.now().strftime("%d-%m-%y")})
        print("Заметка успешно сохранена")


def read_info():
    answer = int(input('Нажмите 1 - прочитать весь файл, 2 - прочитать за опреденную дату, 3 - прочитать по id: '))
    df = pd.read_csv('data.csv', delimiter=";")
    if answer == 1:
        print(df.sort_values(by="Date"))
    elif answer == 2:
        while True:
            data = input('Введите дату в формате день(dd)-месяц(mm)-год(yy): ')
            if re.match(r'\d\d-\d\d-\d\d', data):
                break
            else:
                print('Неверный формат')
        print(df[df["Date"] == data])
    elif answer == 3:
        while True:
            id = int(input("Введите id заметки: "))
            if df["Index"].isin([id]).any():
                print(df[df["Index"] == id])
                break
            else:
                print("Заметки с таким индексом не существует")


def edit_info():
    df = pd.read_csv('data.csv', delimiter=";")
    index_id = int(input("Введите id заметки, которую хотите редактировать: "))
    if df["Index"].isin([index_id]).any():
        anw = int(input("Что хотите подредактировать? 1 - Заголовок, 2 - Содержание:  "))
        while True:
            if anw == 1:
                head_old = df["Title"].values[index_id - 1]
                head_new = input("Введите новый заголовок: ")
                df = df.replace([head_old], head_new)
                df.to_csv('data.csv', index=False, sep=';')
                print("Заголовок успешно изменен")
                break
            elif anw == 2:
                body_old = df["Body"].values[index_id - 1]
                body_new = input("Введите новое содержание: ")
                df = df.replace([body_old], body_new)
                df.to_csv('data.csv', index=False, sep=';')
                print("Содержание успешно изменено")
                break
            else:
                print("Неверный номер. Нажмите 1-заголовок или 2-содержание:  ")
                anw = int(input())
    else:
        print("Такого id нет")


def delete_info():
    index_id = int(input("Введите id заметки, которую хотите удалить: "))
    df = pd.read_csv('data.csv', delimiter=";")
    df = df[df["Index"] != index_id]
    df.to_csv('data.csv', index=False, sep=';')
    print("Данные успешно удалены")