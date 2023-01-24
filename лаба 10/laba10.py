import math
import os
import tkinter.filedialog as fd
from tkinter import Tk, BOTH, StringVar, Text, Menu, END
from tkinter.ttk import Notebook, Frame, Entry, Combobox, Button, Label, Radiobutton, Scrollbar, Style


def calculate():
    number_1 = float(entry_1.get())
    number_2 = float(entry_2.get())
    action = combo.get()
    res = 0
    if action == "+":
        res = number_1 + number_2
    elif action == "-":
        res = number_1 - number_2
    elif action == "*":
        res = number_1 * number_2
    elif action == "/":
        res = number_1 / number_2

    result.configure(text=str((res, int(res))[math.modf(res)[0] == 0]))


def radio():
    t = f'Вы выбрали {selected.get()} вариант'
    rad_res.configure(text=t, width=t.__len__() + 1)


def clear_text():
    text.delete(1.0, END)


def choose_file():
    filename = fd.askopenfilename(
        title="Открыть файл",
        initialdir=os.path.dirname(os.path.abspath(__file__)),
        filetypes=[("Текстовый файл", "*.txt")]
    )
    if filename:
        print(filename)
        with open(filename, 'r') as file:
            text.replace(1.0, END, file.read())
            file.close()


window = Tk()
window.title('Станиславский Сергей Валерьевич')
window.geometry('800x600')

tab_control = Notebook(window)

tab1 = Frame(tab_control)
entry_1 = Entry(tab1, width=10)
entry_1.focus()
entry_2 = Entry(tab1, width=10)
combo = Combobox(tab1, width=2, values=['+', '-', '*', '/'])
button = Button(tab1, text='=', width=2, command=calculate)
result = Label(tab1, width=20)
entry_2.grid(column=2, row=0, padx=5)
entry_1.grid(column=0, row=0, padx=5)
combo.grid(column=1, row=0, padx=5)
button.grid(column=3, row=0, padx=5)
result.grid(column=4, row=0)

tab2 = Frame(tab_control)
selected = StringVar()
selected.set("Первый")
rad1 = Radiobutton(tab2, text='Первый', value="Первый", variable=selected)
rad2 = Radiobutton(tab2, text='Второй', value='Второй', variable=selected)
rad3 = Radiobutton(tab2, text='Третий', value='Третий', variable=selected)
button = Button(tab2, text='Нажми меня', width=12, command=radio)
rad_res = Label(tab2)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
button.grid(column=0, row=1)
rad_res.grid(column=0, row=2, columnspan=3)

tab3 = Frame(tab_control)
text = Text(tab3, width=100, height=100)
ys = Scrollbar(tab3, orient='vertical', command=text.yview)
xs = Scrollbar(tab3, orient='horizontal', command=text.xview)
text['yscrollcommand'] = ys.set
text['xscrollcommand'] = xs.set
text.grid(column=0, row=0, sticky='nwes')
xs.grid(column=0, row=1, sticky='we')
ys.grid(column=1, row=0, sticky='ns')
tab3.grid_columnconfigure(0, weight=1)
tab3.grid_rowconfigure(0, weight=1)
text.option_add('*tearOff', "false")
menu = Menu(text)
menu.add_command(label="Загрузить из файла", command=choose_file)
menu.add_command(label="Очистить", command=clear_text)
if (text.tk.call('tk', 'windowingsystem') == 'aqua'):
    text.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    text.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    text.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))

tab_control.add(tab1, text="Калькулятор")
tab_control.add(tab2, text="Радиобаттон")
tab_control.add(tab3, text="Текст")

tab_control.pack(expand=True, fill=BOTH)

window.mainloop()
