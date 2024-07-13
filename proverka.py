from tkinter import *
from tkinter import messagebox
import random


def game1():
    global KNB
    i = stone.get()
    if i.lower() == 'камень':
        if i.lower() == 'камень' and KNB == 'ножницы':
            label.config(text="Вы победили!\n Ваш противник выбрал ножницы")
            label.place(x=100, y=160)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
        elif i.lower() == 'камень' and KNB == 'камень':
            messagebox.showinfo(title="GAME OVER", message="Ничья. Попробуйте еще раз :)")
            label.config(text=random.choice(['Подумай над тактикой\nВозможно нужно пойти другим путем',
                                             'Внимательно посмотри на противника\nПопробуй предугадать его ход по глазам',
                                             'Вдох-выдох\nСильные противники нас закаляют',
                                             'Действуй! Это твой шанс!']))
            label.place(x=100, y=160)
            KNB = random.choice(['камень', 'ножницы', 'бумага'])
        elif i.lower() == 'камень' and KNB == 'бумага':
            if messagebox.askyesno('GAME OVER',
                                   "Вы проиграли :(\nВаш противник выбрал бумагу\nХотите попробовать еще раз?"):
                label.config(
                    text="Привет!\n Это игра 'Камень, ножницы, бумага'.\nВыбери один из трех предметов,\n и сразись с противником\nПомни, что камень бьет ножницы,\n бумага кроет камень,\n а ножницы режут бумагу.")
                label.place(x=100, y=0)
                KNB = random.choice(['камень', 'ножницы', 'бумага'])
            else:
                label.config(text="Спасибо за игру!\nЖду тебя еще раз ;)")
                label.place(x=200, y=150)
                btn1.destroy()
                btn2.destroy()
                btn3.destroy()
        else:
            label.config(text="Спасибо за игру!\nЖду тебя еще раз ;)")
            label.place(x=200, y=150)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()

    else:
        messagebox.showwarning('WRONG', "Ошибка")
        label.config(text="Ты ввел неккоректное слово\nВыбери камень, ножницы или бумагу")


def game2():
    global KNB
    i = scissors.get()
    if i.lower() == 'ножницы':
        if i.lower() == 'ножницы' and KNB == 'бумага':
            label.config(text="Вы победили!\n Ваш противник выбрал бумагу")
            label.place(x=100, y=160)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
        elif i.lower() == 'ножницы' and KNB == 'ножницы':
            messagebox.showinfo(title="GAME OVER", message="Ничья. Попробуйте еще раз :)")
            label.config(text=random.choice(['Подумай над тактикой\nВозможно нужно пойти другим путем',
                                             'Внимательно посмотри на противника\nПопробуй предугадать его ход по глазам',
                                             'Вдох-выдох\nСильные противники нас закаляют',
                                             'Действуй! Это твой шанс!']))
            label.place(x=100, y=160)
            KNB = random.choice(['камень', 'ножницы', 'бумага'])
        elif i.lower() == 'ножницы' and KNB == 'камень':
            if messagebox.askyesno('GAME OVER',
                                   "Вы проиграли :(\nВаш противник выбрал камень\nХотите попробовать еще раз?"):
                label.config(
                    text="Привет!\n Это игра 'Камень, ножницы, бумага'.\nВыбери один из трех предметов,\n и сразись с противником\nПомни, что камень бьет ножницы,\n бумага кроет камень,\n а ножницы режут бумагу.")
                label.place(x=100, y=0)
                KNB = random.choice(['камень', 'ножницы', 'бумага'])
            else:
                label.config(text="Спасибо за игру!\nЖду тебя еще раз ;)")
                label.place(x=200, y=150)
                btn1.destroy()
                btn2.destroy()
                btn3.destroy()

        else:
            label.config(text="Спасибо за игру!\nЖду тебя еще раз ;)")
            label.place(x=200, y=150)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()

    else:
        messagebox.showwarning('WRONG', "Ошибка")
        label.config(text="Ты ввел неккоректное слово\nВыбери камень, ножницы или бумагу")


def game3():
    global KNB
    i = paper.get()
    if i.lower() == 'бумага':
        if i.lower() == 'бумага' and KNB == 'камень':
            label.config(text="Вы победили!\n Ваш противник выбрал камень")
            label.place(x=100, y=160)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
        elif i.lower() == 'бумага' and KNB == 'бумага':
            messagebox.showinfo(title="GAME OVER", message="Ничья. Попробуйте еще раз :)")
            label.config(text=random.choice(['Подумай над тактикой\nВозможно нужно пойти другим путем',
                                             'Внимательно посмотри на противника\nПопробуй предугадать его ход по глазам',
                                             'Вдох-выдох\nСильные противники нас закаляют',
                                             'Действуй! Это твой шанс!']))
            label.place(x=100, y=160)
            KNB = random.choice(['камень', 'ножницы', 'бумага'])
        elif i.lower() == 'бумага' and KNB == 'ножницы':
            if messagebox.askyesno('GAME OVER',
                                   "Вы проиграли :(\nВаш противник выбрал бумагу\nХотите попробовать еще раз?"):
                label.config(
                    text="Привет!\n Это игра 'Камень, ножницы, бумага'.\nВыбери один из трех предметов,\n и сразись с противником\nПомни, что камень бьет ножницы,\n бумага кроет камень,\n а ножницы режут бумагу.")
                label.place(x=100, y=0)
                KNB = random.choice(['камень', 'ножницы', 'бумага'])
            else:
                label.config(text="Спасибо за игру!\nЖду тебя еще раз ;)")
                label.place(x=200, y=150)
                btn1.destroy()
                btn2.destroy()
                btn3.destroy()
        else:
            label.config(text="Спасибо за игру!\nЖду тебя еще раз ;)")
            label.place(x=200, y=150)
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()

    else:
        messagebox.showwarning('WRONG', "Ошибка")
        label.config(text="Ты ввел неккоректное слово\nВыбери камень, ножницы или бумагу")


window = Tk()
KNB = random.choice(['камень', 'ножницы', 'бумага'])
stone = StringVar(value="Камень")
scissors = StringVar(value="Ножницы")
paper = StringVar(value="Бумага")
window.geometry('900x450')
window.title("Игра 'Камень, ножницы, бумага'")
label = Label(window,
              text="Привет!\n Это игра 'Камень, ножницы, бумага'.\nВыбери один из трех предметов,\n и сразись с противником\nПомни, что камень бьет ножницы,\n бумага кроет камень,\n а ножницы режут бумагу.",
              font=("Arial Bold", 30))
label.place(x=100, y=0)
btn1 = Button(window, font=("Arial Bold", 20), bg="black", fg="white", command=game1, textvariable=stone)
btn1.place(x=350, y=330, width=130, height=70)
btn2 = Button(window, text="Ножницы", font=("Arial Bold", 20), bg="black", fg="white", command=game2,
              textvariable=scissors)
btn2.place(x=140, y=330, width=130, height=70)
btn3 = Button(window, text="Бумага", font=("Arial Bold", 20), bg="black", fg="white", command=game3, textvariable=paper)
btn3.place(x=570, y=330, width=130, height=70)
window.mainloop()
