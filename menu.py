from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Radiobutton  
window = Tk()
window.title("Smart-cinema")
window.geometry("750x600")
window.resizable(width=False, height=False) 
window['bg'] = "white"
fon = IntVar()
fon.set(0)

def onClick():

    bron = tk.Toplevel(window)
    bron.title("Бронирование мест 'Batman'")
    bron.geometry("400x350")
    bron.resizable(width=False, height=False)
    bron['bg'] = window['bg']
    lb3 = Label(bron, text="Выберите сеанс", bg="white", font="Arial 15")
    lb3.place(x=127, y=20)
    lb4 = Label(bron, text='День', bg='white')
    lb4.place(x=70, y=60)
    combo = Combobox(bron)
    combo['values'] = ("07.03.2022", "08.03.2022")
    combo.place(x=20, y=80)
    lb5 = Label(bron, text='Время', bg='white')
    lb5.place(x=285, y=60)
    combo1 = Combobox(bron)
    combo1['values'] = ("15:00", "18:00")
    combo1.place(x=235, y=80)
    lb2 = Label(bron, text="Кинозал", bg="white", font="Arial 15")
    lb2.place(x=160, y=120)
    radb1 = Radiobutton(bron, text="Кинозал #1", value=1)
    radb2 = Radiobutton(bron, text="Кинозал #2", value=2)
    radb3 = Radiobutton(bron, text="Кинозал #3", value=3)
    radb1.place(x=40, y=175)
    radb2.place(x=160, y=175)
    radb3.place(x=280, y=175)
    def places():
    	place = tk.Toplevel(bron)
    	place.title("Выбрать место на фильм Batman")
    	place.geometry("700x350")
    	place.resizable(width=False, height=False)
    btn = Button(bron, text="Выбрать места", font="Arial 15", command=places)
    btn.place(x=120, y=220)
    def Acces():
    	acces = tk.Toplevel(bron)
    	acces.title("Успех")
    	acces.geometry("220x150")
    	acces.resizable(width=False, height=False)
    	acces_lb = Label(acces, text="Вы успешно забронировали места")
    	acces_lb.place(x=14, y=30)
    	acces_btn = Button(acces, text="OK", width=20, command=acces.destroy)
    	acces_btn.place(x=40, y=85)
    btn1 = Button(bron, text="Забронировать места", font="Arial 15", command=Acces)
    btn1.place(x=90, y=280)



def onClick1():
	
    bron1 = tk.Toplevel(window)
    bron1.title("Бронирование мест 'Martan'")
    bron1.geometry("400x350")
    bron1.resizable(width=False, height=False)
    bron1['bg'] = window['bg']

def onClick2():
	
    bron2 = tk.Toplevel(window)
    bron2.title("Бронирование мест 'Чудо-женщина'")
    bron2.geometry("400x350")
    bron2.resizable(width=False, height=False)
    bron2['bg'] = window['bg']

def onClick3():
	
    bron3 = tk.Toplevel(window)
    bron3.title("Бронирование мест 'На игре'")
    bron3.geometry("400x350")
    bron3.resizable(width=False, height=False)
    bron3['bg'] = window['bg']        

def onClick4():
	
    bron4 = tk.Toplevel(window)
    bron4.title("Бронирование мест 'Люди-Икс'")
    bron4.geometry("400x350")
    bron4.resizable(width=False, height=False)
    bron4['bg'] = window['bg']

def onClick5():
	
    bron5 = tk.Toplevel(window)
    bron5.title("Бронирование мест 'Прометей'")
    bron5.geometry("400x350")
    bron5.resizable(width=False, height=False)
    bron5['bg'] = window['bg']

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

class Movies():
	def __init__(self):
		lbl = Label(window, text="Фильмы")
	b = Button(window, command=onClick, fg="white", bg = "white")
	b1 = Button(window, command=onClick1, fg="white", bg = "white")
	b2 = Button(window, command=onClick2, fg="white", bg = "white")
	b3 = Button(window, command=onClick3, fg="white", bg = "white")
	b4 = Button(window, command=onClick4, fg="white", bg = "white")
	b5 = Button(window, command=onClick5, fg="white", bg = "white")
	b.place(x=10,y=20)
	b1.place(x=270,y=20)
	b2.place(x=530,y=20)
	b3.place(x=10,y=300)
	b4.place(x=270,y=300)
	b5.place(x=530,y=300)

	image = Image.open("batman.png")
	photo = ImageTk.PhotoImage(image)
	image1 = Image.open("mars.png")
	photo1 = ImageTk.PhotoImage(image1)
	image2 = Image.open("women.png")
	photo2 = ImageTk.PhotoImage(image2)
	image3 = Image.open("naigre.png")
	photo3 = ImageTk.PhotoImage(image3)
	image4 = Image.open("xmen.png")
	photo4 = ImageTk.PhotoImage(image4)
	image5 = Image.open("prometei.png")
	photo5 = ImageTk.PhotoImage(image5)
	b.config(image=photo)
	b1.config(image=photo1)
	b2.config(image=photo2)
	b3.config(image=photo3)
	b4.config(image=photo4)
	b5.config(image=photo5)



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
    movie = Movies()
    window.mainloop()
    

