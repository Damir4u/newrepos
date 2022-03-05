from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
window = Tk()
window.title("Smart-cinema")
window.geometry("500x500")
window.resizable(width=False, height=False) 
window['bg'] = "white"
fon = IntVar()
fon.set(0)
class Panel():
    def __init__(self):
        super().__init__()
        menu = Menu(window)
        file_menu = Menu(menu, tearoff=0)
        view = Menu(menu, tearoff=0)
        spravka = Menu(menu, tearoff=0)

        file_menu.add_command(label="Билеты")
        file_menu.add_command(label="Фильмы")
        file_menu.add_command(label="Залы")

        view.add_radiobutton(label="Светлый режим", variable=fon, value= 1, command=change_view)
        view.add_radiobutton(label="Темный режим", variable=fon, value= 2, command=change_view)

        spravka.add_command(label="Просмотреть справку")
        spravka.add_separator()
        spravka.add_command(label="О программе", command=about_programm)

        menu.add_cascade(label="Данные", menu=file_menu)
        menu.add_cascade(label="Вид", menu=view)
        menu.add_cascade(label="Справка", menu=spravka)
        menu.add_command(label="Выход", command=window.destroy)
        window.config(menu=menu)

def change_view():
    if fon.get() == 1:
        window['bg'] = "white"
    elif fon.get() == 2:
        window['bg'] = "black"
         

def about_programm():
    programm = tk.Toplevel(window)
    programm.title('О программе "Smart-cinema"')
    programm.geometry("400x350")
    programm.resizable(width=False, height=False)
    programm['bg'] = "white"
    canvas = Canvas(programm, width = 400, height=350, bg='white') 
    canvas.pack()
    logo = PhotoImage(file="logo.png")
    canvas.create_image(125,0,anchor=NW,image=logo)
    canvas.create_text(200,140,fill="black", font="Arial", text="Это приложение позволяющие с легкостью")
    canvas.create_text(201,160,fill="black", font="Arial", text="анализировать данные нашего кинотеатра.")
    canvas.create_text(182,180,fill="black", font="Arial", text="Узнавать самые популярные фильмы")
    canvas.create_text(180,200,fill="black", font="Arial", text="количество проданных билетов и т.д.")
    canvas.create_text(200,250,fill="black", font="Arial", text="Разработчики:")
    canvas.create_text(200,270,fill="black", font="Arial", text="Хандрико К.В. Суендыков Д.Ж.")
    canvas.create_text(200,290,fill="black", font="Arial", text="Бондаренко С.С. Едельбаев Д.")
    programm.mainloop()



if __name__ == "__main__":
    app = Panel()
    window.mainloop()

