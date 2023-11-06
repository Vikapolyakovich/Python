import os.path

from algoritm import *
from work_w_file import *
from os import path

if not path.exists("data.csv") or os.path.getsize("data.csv") == 0:
    with open("data.csv", mode="w", encoding='utf-8') as w_file:
        names = ["Index", "Title", "Body", "Date"]
        file_writer = csv.DictWriter(w_file, delimiter=";",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writeheader()


while True:
    print_instructions()
    choose(input("Введите команду: "))