# 9. Automattic WordPress Calypso
# JavaScript и API-интерфейс для WordPress.com
# Репозиторий: https://github.com/Automattic/wp-calypso
# Веб-сайт: https://developer.wordpress.com/calypso

import json
import re
from tkinter import Tk
from tkinter.ttk import Entry, Label, Button

import requests


def extract_username(url: str):
    return re.compile('https://github.com/(.*)/.*').findall(url)[0]


def transfor_json(json_: dict):
    res = {}
    for field in ['company', 'created_at', 'email', 'id', 'name', 'url']:
        res[field] = json_.get(field)

    return res


def save_to_file():
    json_ = transfor_json(requests.get(f'https://api.github.com/users/{extract_username(entry.get())}').json())
    file_name = '_'.join([json_.get('name'), str(json_.get('id'))]) + '.txt'
    with open(file_name, 'w') as file:
        json.dump(json_, file, indent=4)
        file.close()
    res_label.configure(text=f'json сохранён в файл {file_name}')


window = Tk()
window.title('Загрузка json')
window.configure(border=10)
lable = Label(window, text="Введите url репозитория на github: ")
lable.grid(column=0, row=0)
entry = Entry(window, width=50)
entry.grid(column=1, row=0, padx=5)
button = Button(window, text="Загрузить в файл", command=save_to_file)
button.grid(column=2, row=0, padx=5)
res_label = Label(window)
res_label.grid(column=0, row=1)

window.mainloop()
