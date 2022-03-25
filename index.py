import sys
import time
from datetime import date
from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Radiobutton  
import tkinter.ttk as ttk
import openpyxl
date = date.today()
window = Tk()
window.title("Smart-cinema")
window.attributes('-fullscreen', True)
db = openpyxl.load_workbook('database.xlsx')
sheets = db.sheetnames
sheet = db.active
fon = IntVar()
fon.set(1)
var = IntVar()
var.set(0)
point = IntVar()
point.set(0)



class View():
	global clock
	global today
	def change_view():
		if fon.get() == 1:
			Movies.box['bg'] = "azure3"
			Movies.box.itemconfig('lines',fill="black")
			View.s.configure('Wild.TRadiobutton', background="azure3", foreground="black", font=("Arial", 30))
			Movies.seansi.config(bg="azure3", foreground="black", font=("Arial",30))
			Movies.btn_time1.config(bg="azure3",fg='black', font=("Arial", 30))
			Movies.btn_time2.config(bg="azure3",fg='black', font=("Arial", 30))
			Movies.btn_time3.config(bg="azure3",fg='black', font=("Arial", 30))
			Movies.btn_time4.config(bg="azure3",fg='black', font=("Arial", 30))
			Movies.btn_time5.config(bg="azure3",fg='black', font=("Arial", 30))
			Movies.btn_time6.config(bg="azure3",fg='black', font=("Arial", 30))
			Movies.back.config(bg="azure3",fg='black', font=("Arial", 20))
			Movies.cancel.config(bg="azure3",fg='black', font=("Arial", 20))
			Movies.lbl_place.config(bg="azure3",fg='black', font=("Arial", 30))
			clock.config(bg="azure3",fg='black', font=("times",30,"bold"))
			today.config(bg="azure3",fg='black', font=("times",30,"bold"))
		elif fon.get() == 2:
			Movies.box['bg'] = "#333333" 
			Movies.box.itemconfig('lines',fill="white")
			View.s1.configure('Wild.TRadiobutton', background="#333333", foreground="white", font=("Courier",30))
			Movies.seansi.config(bg="#333333", foreground="white", font=("Courier",30))
			Movies.btn_time1.config(bg="#333333",fg='white', font=("Courier",30))
			Movies.btn_time2.config(bg="#333333",fg='white', font=("Courier",30))
			Movies.btn_time3.config(bg="#333333",fg='white', font=("Courier",30))
			Movies.btn_time4.config(bg="#333333",fg='white', font=("Courier",30))
			Movies.btn_time5.config(bg="#333333",fg='white', font=("Courier",30))
			Movies.btn_time6.config(bg="#333333",fg='white', font=("Courier",30))
			Movies.back.config(bg="#333333",fg='white', font=("Courier",20))
			Movies.cancel.config(bg="#333333",fg='white', font=("Courier",20))
			Movies.lbl_place.config(bg="#333333",fg='white', font=("Courier",30))
			clock.config(bg="#333333",fg='white', font=("Courier",30))
			today.config(bg="#333333",fg='white', font=("Courier",30))
	white_color = "azure3"
	black_color = '#333333'
	s1 = ttk.Style()
	s = ttk.Style()
	s.configure('Wild.TRadiobutton', background=white_color, foreground="black", width="10", height="20", font=("Arial", 30))


class Panel():
	def __init__(self):
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
			canvas.create_text(200,140,fill="black", font="Arial 12", text="Это приложение позволяющие с легкостью")
			canvas.create_text(201,160,fill="black", font="Arial 12", text="анализировать данные нашего кинотеатра.")
			canvas.create_text(182,180,fill="black", font="Arial 12", text="Узнавать самые популярные фильмы")
			canvas.create_text(180,200,fill="black", font="Arial 12", text="количество проданных билетов и т.д.")
			canvas.create_text(200,250,fill="black", font="Arial 12", text="Разработчики:")
			canvas.create_text(200,270,fill="black", font="Arial 12", text="Хандрико К.В. Суендыков Д.Ж.")
			canvas.create_text(200,290,fill="black", font="Arial 12", text="Бондаренко С.С. Едельбаев Д.")
			programm.mainloop()



		def check_places():
			def proverka():
				i = 0
				if (sheet['B2'].value) == 1:
					i += 1
				if (sheet['C2'].value) == 1:
					i += 1
				if (sheet['D2'].value) == 1:
					i += 1
				if (sheet['E2'].value) == 1:
					i += 1
				if (sheet['F2'].value) == 1:
					i += 1
				if (sheet['B3'].value) == 1:
					i += 1
				if (sheet['C3'].value) == 1:
					i += 1
				if (sheet['D3'].value) == 1:
					i += 1
				if (sheet['E3'].value) == 1:
					i += 1
				if (sheet['F3'].value) == 1:
					i += 1
				if (sheet['B4'].value) == 1:
					i += 1
				if (sheet['C4'].value) == 1:
					i += 1
				if (sheet['D4'].value) == 1:
					i += 1
				if (sheet['E4'].value) == 1:
					i += 1
				if (sheet['F4'].value) == 1:
					i += 1
				if (sheet['B5'].value) == 1:
					i += 1
				if (sheet['C5'].value) == 1:
					i += 1
				if (sheet['D5'].value) == 1:
					i += 1
				if (sheet['E5'].value) == 1:
					i += 1
				if (sheet['F5'].value) == 1:
					i += 1
				if (sheet['B8'].value) == 1:
					i += 1
				if (sheet['C8'].value) == 1:
					i += 1
				if (sheet['D8'].value) == 1:
					i += 1
				if (sheet['E8'].value) == 1:
					i += 1
				if (sheet['F8'].value) == 1:
					i += 1
				if (sheet['B9'].value) == 1:
					i += 1
				if (sheet['C9'].value) == 1:
					i += 1
				if (sheet['D9'].value) == 1:
					i += 1
				if (sheet['E9'].value) == 1:
					i += 1
				if (sheet['F9'].value) == 1:
					i += 1
				if (sheet['B10'].value) == 1:
					i += 1
				if (sheet['C10'].value) == 1:
					i += 1
				if (sheet['D10'].value) == 1:
					i += 1
				if (sheet['E10'].value) == 1:
					i += 1
				if (sheet['F10'].value) == 1:
					i += 1
				if (sheet['B11'].value) == 1:
					i += 1
				if (sheet['C11'].value) == 1:
					i += 1
				if (sheet['D11'].value) == 1:
					i += 1
				if (sheet['E11'].value) == 1:
					i += 1
				if (sheet['F11'].value) == 1:
					i += 1
				sa = Label(window_places, text="Количество заполненных мест в кинозале 1:", bg='azure3', font=("Arial", 17))
				kkk = Label(window_places, text=i, bg="azure3", font=("Arial", 17))
				sa.place(x=120,y=150)
				kkk.place(x=600,y=150)

			def proverka1():
				i = 0
				if (sheet['I2'].value) == 1:
					i += 1
				if (sheet['J2'].value) == 1:
					i += 1
				if (sheet['K2'].value) == 1:
					i += 1
				if (sheet['L2'].value) == 1:
					i += 1
				if (sheet['M2'].value) == 1:
					i += 1
				if (sheet['I3'].value) == 1:
					i += 1
				if (sheet['J3'].value) == 1:
					i += 1
				if (sheet['K3'].value) == 1:
					i += 1
				if (sheet['L3'].value) == 1:
					i += 1
				if (sheet['M3'].value) == 1:
					i += 1
				if (sheet['I4'].value) == 1:
					i += 1
				if (sheet['J4'].value) == 1:
					i += 1
				if (sheet['K4'].value) == 1:
					i += 1
				if (sheet['L4'].value) == 1:
					i += 1
				if (sheet['M4'].value) == 1:
					i += 1
				if (sheet['I5'].value) == 1:
					i += 1
				if (sheet['J5'].value) == 1:
					i += 1
				if (sheet['K5'].value) == 1:
					i += 1
				if (sheet['L5'].value) == 1:
					i += 1
				if (sheet['M5'].value) == 1:
					i += 1
				if (sheet['I8'].value) == 1:
					i += 1
				if (sheet['J8'].value) == 1:
					i += 1
				if (sheet['K8'].value) == 1:
					i += 1
				if (sheet['L8'].value) == 1:
					i += 1
				if (sheet['M8'].value) == 1:
					i += 1
				if (sheet['I9'].value) == 1:
					i += 1
				if (sheet['J9'].value) == 1:
					i += 1
				if (sheet['K9'].value) == 1:
					i += 1
				if (sheet['L9'].value) == 1:
					i += 1
				if (sheet['M9'].value) == 1:
					i += 1
				if (sheet['I10'].value) == 1:
					i += 1
				if (sheet['J10'].value) == 1:
					i += 1
				if (sheet['K10'].value) == 1:
					i += 1
				if (sheet['L10'].value) == 1:
					i += 1
				if (sheet['M10'].value) == 1:
					i += 1
				if (sheet['I11'].value) == 1:
					i += 1
				if (sheet['J11'].value) == 1:
					i += 1
				if (sheet['K11'].value) == 1:
					i += 1
				if (sheet['L11'].value) == 1:
					i += 1
				if (sheet['M11'].value) == 1:
					i += 1
				sa1 = Label(window_places, text="Количество заполненных мест в кинозале 2:", bg='azure3', font=("Arial", 17))
				kkk1 = Label(window_places, text=i, bg="azure3", font=("Arial", 17))
				sa1.place(x=120,y=150)
				kkk1.place(x=600,y=150)

			def clear():
				i = 0
				if (sheet['B2'].value) == 1:
					i += 1
				if (sheet['C2'].value) == 1:
					i += 1
				if (sheet['D2'].value) == 1:
					i += 1
				if (sheet['E2'].value) == 1:
					i += 1
				if (sheet['F2'].value) == 1:
					i += 1
				if (sheet['B3'].value) == 1:
					i += 1
				if (sheet['C3'].value) == 1:
					i += 1
				if (sheet['D3'].value) == 1:
					i += 1
				if (sheet['E3'].value) == 1:
					i += 1
				if (sheet['F3'].value) == 1:
					i += 1
				if (sheet['B4'].value) == 1:
					i += 1
				if (sheet['C4'].value) == 1:
					i += 1
				if (sheet['D4'].value) == 1:
					i += 1
				if (sheet['E4'].value) == 1:
					i += 1
				if (sheet['F4'].value) == 1:
					i += 1
				if (sheet['B5'].value) == 1:
					i += 1
				if (sheet['C5'].value) == 1:
					i += 1
				if (sheet['D5'].value) == 1:
					i += 1
				if (sheet['E5'].value) == 1:
					i += 1
				if (sheet['F5'].value) == 1:
					i += 1
				if (sheet['B8'].value) == 1:
					i += 1
				if (sheet['C8'].value) == 1:
					i += 1
				if (sheet['D8'].value) == 1:
					i += 1
				if (sheet['E8'].value) == 1:
					i += 1
				if (sheet['F8'].value) == 1:
					i += 1
				if (sheet['B9'].value) == 1:
					i += 1
				if (sheet['C9'].value) == 1:
					i += 1
				if (sheet['D9'].value) == 1:
					i += 1
				if (sheet['E9'].value) == 1:
					i += 1
				if (sheet['F9'].value) == 1:
					i += 1
				if (sheet['B10'].value) == 1:
					i += 1
				if (sheet['C10'].value) == 1:
					i += 1
				if (sheet['D10'].value) == 1:
					i += 1
				if (sheet['E10'].value) == 1:
					i += 1
				if (sheet['F10'].value) == 1:
					i += 1
				if (sheet['B11'].value) == 1:
					i += 1
				if (sheet['C11'].value) == 1:
					i += 1
				if (sheet['D11'].value) == 1:
					i += 1
				if (sheet['E11'].value) == 1:
					i += 1
				if (sheet['F11'].value) == 1:
					i += 1
				if (sheet['I2'].value) == 1:
					i += 1
				if (sheet['J2'].value) == 1:
					i += 1
				if (sheet['K2'].value) == 1:
					i += 1
				if (sheet['L2'].value) == 1:
					i += 1
				if (sheet['M2'].value) == 1:
					i += 1
				if (sheet['I3'].value) == 1:
					i += 1
				if (sheet['J3'].value) == 1:
					i += 1
				if (sheet['K3'].value) == 1:
					i += 1
				if (sheet['L3'].value) == 1:
					i += 1
				if (sheet['M3'].value) == 1:
					i += 1
				if (sheet['I4'].value) == 1:
					i += 1
				if (sheet['J4'].value) == 1:
					i += 1
				if (sheet['K4'].value) == 1:
					i += 1
				if (sheet['L4'].value) == 1:
					i += 1
				if (sheet['M4'].value) == 1:
					i += 1
				if (sheet['I5'].value) == 1:
					i += 1
				if (sheet['J5'].value) == 1:
					i += 1
				if (sheet['K5'].value) == 1:
					i += 1
				if (sheet['L5'].value) == 1:
					i += 1
				if (sheet['M5'].value) == 1:
					i += 1
				if (sheet['I8'].value) == 1:
					i += 1
				if (sheet['J8'].value) == 1:
					i += 1
				if (sheet['K8'].value) == 1:
					i += 1
				if (sheet['L8'].value) == 1:
					i += 1
				if (sheet['M8'].value) == 1:
					i += 1
				if (sheet['I9'].value) == 1:
					i += 1
				if (sheet['J9'].value) == 1:
					i += 1
				if (sheet['K9'].value) == 1:
					i += 1
				if (sheet['L9'].value) == 1:
					i += 1
				if (sheet['M9'].value) == 1:
					i += 1
				if (sheet['I10'].value) == 1:
					i += 1
				if (sheet['J10'].value) == 1:
					i += 1
				if (sheet['K10'].value) == 1:
					i += 1
				if (sheet['L10'].value) == 1:
					i += 1
				if (sheet['M10'].value) == 1:
					i += 1
				if (sheet['I11'].value) == 1:
					i += 1
				if (sheet['J11'].value) == 1:
					i += 1
				if (sheet['K11'].value) == 1:
					i += 1
				if (sheet['L11'].value) == 1:
					i += 1
				if (sheet['M11'].value) == 1:
					i += 1
				sa11 = Label(window_places, text="Количество заполненных мест во всех кинозалах:", bg='azure3', font=("Arial", 17))
				kkk11 = Label(window_places, text=i, bg="azure3", font=("Arial", 17))
				sa11.place(x=100,y=270)
				kkk11.place(x=660,y=270)




			window_places = tk.Toplevel(window)
			window_places.title('Заполненные места')
			window_places.geometry("780x350")
			window_places.resizable(width=False, height=False)
			window_places['bg'] = "azure3"
			lll = Label(window_places, text="Выберите кинозал", font=("Arial", 30), bg='azure3')
			cl = Button(window_places, text="Узнать количество людей во всех кинозалах", width=40, bg='azure3', font=('Arial', 20), command=clear)
			rdbtn1 = Radiobutton(window_places, text="Кинозал 1", variable=point, value=1, width=9, style='Wild.TRadiobutton', command=proverka)
			rdbtn2 = Radiobutton(window_places, text="Кинозал 2", variable=point, value=2, width=9, style='Wild.TRadiobutton', command=proverka1)
			rdbtn3 = Radiobutton(window_places, text="Кинозал 3", variable=point, value=3, width=9, style='Wild.TRadiobutton')
			rdbtn1.place(x=10, y=80)
			rdbtn2.place(x=280, y=80)
			rdbtn3.place(x=550, y=80)
			cl.place(x=65,y=210)
			lll.place(x=200,y=20)
			window_places.mainloop()

		def info():
			os.system('123.docx')

		menu = Menu(window)
		file_menu = Menu(menu, tearoff=0)
		view = Menu(menu, tearoff=0)
		spravka = Menu(menu, tearoff=0)

		file_menu.add_command(label="Места", command=check_places)

		view.add_radiobutton(label="Светлый режим", variable=fon, value= 1, command=View.change_view)
		view.add_radiobutton(label="Темный режим", variable=fon, value= 2, command=View.change_view)

		spravka.add_command(label="Просмотреть справку", command=info)
		spravka.add_separator()
		spravka.add_command(label="О программе", command=about_programm)

		menu.add_cascade(label="Данные", menu=file_menu)
		menu.add_cascade(label="Вид", menu=view)
		menu.add_cascade(label="Справка", menu=spravka)
		menu.add_command(label="Выход", command=window.destroy)
		window.config(menu=menu)

class Movies():

	def cancel():
		Movies.box.itemconfig('1a', fill="azure3")
		Movies.box.itemconfig('2a', fill="azure3")
		Movies.box.itemconfig('3a', fill="azure3")
		Movies.box.itemconfig('4a', fill="azure3")
		Movies.back.place_forget()
		Movies.kinozal_rdbtn1.place_forget()
		Movies.kinozal_rdbtn2.place_forget()
		Movies.kinozal_rdbtn3.place_forget()
		Movies.btn_time1.place_forget()
		Movies.btn_time2.place_forget()
		Movies.btn_time3.place_forget()
		Movies.btn_time4.place_forget()
		Movies.btn_time5.place_forget()
		Movies.btn_time6.place_forget()
		Movies.cancel.place_forget()
		Movies.lbl_place.place_forget()
		Movies.btn_place1.place_forget()
		Movies.btn_place2.place_forget()
		Movies.btn_place3.place_forget()
		Movies.btn_place4.place_forget()
		Movies.btn_place5.place_forget()
		Movies.btn_place6.place_forget()
		Movies.btn_place7.place_forget()
		Movies.btn_place8.place_forget()
		Movies.btn_place9.place_forget()
		Movies.btn_place10.place_forget()
		Movies.btn_place11.place_forget()
		Movies.btn_place12.place_forget()
		Movies.btn_place13.place_forget()
		Movies.btn_place14.place_forget()
		Movies.btn_place15.place_forget()
		Movies.btn_place16.place_forget()
		Movies.btn_place17.place_forget()
		Movies.btn_place18.place_forget()
		Movies.btn_place19.place_forget()
		Movies.btn_place20.place_forget()
		Movies.btn_place21.place_forget()
		Movies.btn_place22.place_forget()
		Movies.btn_place23.place_forget()
		Movies.btn_place24.place_forget()
		Movies.btn_place25.place_forget()
		Movies.btn_place26.place_forget()
		Movies.btn_place27.place_forget()
		Movies.btn_place28.place_forget()
		Movies.btn_place29.place_forget()
		Movies.btn_place30.place_forget()
		Movies.btn_place31.place_forget()
		Movies.btn_place32.place_forget()
		Movies.btn_place33.place_forget()
		Movies.btn_place34.place_forget()
		Movies.btn_place35.place_forget()
		Movies.btn_place36.place_forget()
		Movies.btn_place37.place_forget()
		Movies.btn_place38.place_forget()
		Movies.btn_place39.place_forget()
		Movies.btn_place40.place_forget()
		Movies.btn_place41.place_forget()
		Movies.btn_place42.place_forget()
		Movies.btn_place43.place_forget()
		Movies.btn_place44.place_forget()
		Movies.btn_place45.place_forget()
		Movies.btn_place46.place_forget()
		Movies.btn_place47.place_forget()
		Movies.btn_place48.place_forget()
		Movies.btn_place49.place_forget()
		Movies.btn_place50.place_forget()
		Movies.btn_place51.place_forget()
		Movies.btn_place52.place_forget()
		Movies.btn_place53.place_forget()
		Movies.btn_place54.place_forget()
		Movies.btn_place55.place_forget()
		Movies.btn_place56.place_forget()
		Movies.btn_place57.place_forget()
		Movies.btn_place58.place_forget()
		Movies.btn_place59.place_forget()
		Movies.btn_place60.place_forget()
		Movies.btn_place61.place_forget()
		Movies.btn_place62.place_forget()
		Movies.btn_place63.place_forget()
		Movies.btn_place64.place_forget()
		Movies.btn_place65.place_forget()
		Movies.btn_place66.place_forget()
		Movies.btn_place67.place_forget()
		Movies.btn_place68.place_forget()
		Movies.btn_place69.place_forget()
		Movies.btn_place70.place_forget()
		Movies.btn_place71.place_forget()
		Movies.btn_place72.place_forget()
		Movies.btn_place73.place_forget()
		Movies.btn_place74.place_forget()
		Movies.btn_place75.place_forget()
		Movies.btn_place76.place_forget()
		Movies.btn_place77.place_forget()
		Movies.btn_place78.place_forget()
		Movies.btn_place79.place_forget()
		Movies.btn_place80.place_forget()
		Movies.btn_place81.place_forget()
		Movies.btn_place82.place_forget()
		Movies.btn_place83.place_forget()
		Movies.btn_place84.place_forget()
		Movies.btn_place85.place_forget()
		Movies.btn_place86.place_forget()
		Movies.btn_place87.place_forget()
		Movies.btn_place88.place_forget()
		Movies.btn_place89.place_forget()
		Movies.btn_place90.place_forget()
		Movies.btn_place91.place_forget()
		Movies.btn_place92.place_forget()
		Movies.btn_place93.place_forget()
		Movies.btn_place94.place_forget()
		Movies.btn_place95.place_forget()
		Movies.btn_place96.place_forget()
		Movies.btn_place97.place_forget()
		Movies.btn_place98.place_forget()
		Movies.btn_place99.place_forget()
		Movies.btn_place100.place_forget()
		Movies.btn_place101.place_forget()
		Movies.btn_place102.place_forget()
		Movies.btn_place103.place_forget()
		Movies.btn_place104.place_forget()
		Movies.btn_place105.place_forget()
		Movies.btn_place106.place_forget()
		Movies.btn_place107.place_forget()
		Movies.btn_place108.place_forget()
		Movies.btn_place109.place_forget()
		Movies.btn_place110.place_forget()
		Movies.btn_place111.place_forget()
		Movies.btn_place112.place_forget()
		Movies.btn_place113.place_forget()
		Movies.btn_place114.place_forget()
		Movies.btn_place115.place_forget()
		Movies.btn_place116.place_forget()
		Movies.btn_place117.place_forget()
		Movies.btn_place118.place_forget()
		Movies.btn_place119.place_forget()
		Movies.btn_place120.place_forget()
		Movies.btn_place121.place_forget()
		Movies.btn_place122.place_forget()
		Movies.btn_place123.place_forget()
		Movies.btn_place124.place_forget()
		Movies.btn_place125.place_forget()
		Movies.btn_place126.place_forget()
		Movies.btn_place127.place_forget()
		Movies.btn_place128.place_forget()
		Movies.btn_place129.place_forget()
		Movies.btn_place130.place_forget()
		Movies.btn_place131.place_forget()
		Movies.btn_place132.place_forget()
		Movies.btn_place133.place_forget()
		Movies.btn_place134.place_forget()
		Movies.btn_place135.place_forget()
		Movies.btn_place136.place_forget()
		Movies.btn_place137.place_forget()
		Movies.btn_place138.place_forget()
		Movies.btn_place139.place_forget()
		Movies.btn_place140.place_forget()
		Movies.btn_place141.place_forget()
		Movies.btn_place142.place_forget()
		Movies.btn_place143.place_forget()
		Movies.btn_place144.place_forget()
		Movies.btn_place145.place_forget()
		Movies.btn_place146.place_forget()
		Movies.btn_place147.place_forget()
		Movies.btn_place148.place_forget()
		Movies.btn_place149.place_forget()
		Movies.btn_place150.place_forget()
		Movies.btn_place151.place_forget()
		Movies.btn_place152.place_forget()
		Movies.btn_place153.place_forget()
		Movies.btn_place154.place_forget()
		Movies.btn_place155.place_forget()
		Movies.btn_place156.place_forget()
		Movies.btn_place157.place_forget()
		Movies.btn_place158.place_forget()
		Movies.btn_place159.place_forget()
		Movies.btn_place160.place_forget()

	def back():
		Movies.back.place_forget()
		Movies.lbl_place.place_forget()
		Movies.btn_place1.place_forget()
		Movies.btn_place2.place_forget()
		Movies.btn_place3.place_forget()
		Movies.btn_place4.place_forget()
		Movies.btn_place5.place_forget()
		Movies.btn_place6.place_forget()
		Movies.btn_place7.place_forget()
		Movies.btn_place8.place_forget()
		Movies.btn_place9.place_forget()
		Movies.btn_place10.place_forget()
		Movies.btn_place11.place_forget()
		Movies.btn_place12.place_forget()
		Movies.btn_place13.place_forget()
		Movies.btn_place14.place_forget()
		Movies.btn_place15.place_forget()
		Movies.btn_place16.place_forget()
		Movies.btn_place17.place_forget()
		Movies.btn_place18.place_forget()
		Movies.btn_place19.place_forget()
		Movies.btn_place20.place_forget()
		Movies.btn_place21.place_forget()
		Movies.btn_place22.place_forget()
		Movies.btn_place23.place_forget()
		Movies.btn_place24.place_forget()
		Movies.btn_place25.place_forget()
		Movies.btn_place26.place_forget()
		Movies.btn_place27.place_forget()
		Movies.btn_place28.place_forget()
		Movies.btn_place29.place_forget()
		Movies.btn_place30.place_forget()
		Movies.btn_place31.place_forget()
		Movies.btn_place32.place_forget()
		Movies.btn_place33.place_forget()
		Movies.btn_place34.place_forget()
		Movies.btn_place35.place_forget()
		Movies.btn_place36.place_forget()
		Movies.btn_place37.place_forget()
		Movies.btn_place38.place_forget()
		Movies.btn_place39.place_forget()
		Movies.btn_place40.place_forget()
		Movies.btn_place41.place_forget()
		Movies.btn_place42.place_forget()
		Movies.btn_place43.place_forget()
		Movies.btn_place44.place_forget()
		Movies.btn_place45.place_forget()
		Movies.btn_place46.place_forget()
		Movies.btn_place47.place_forget()
		Movies.btn_place48.place_forget()
		Movies.btn_place49.place_forget()
		Movies.btn_place50.place_forget()
		Movies.btn_place51.place_forget()
		Movies.btn_place52.place_forget()
		Movies.btn_place53.place_forget()
		Movies.btn_place54.place_forget()
		Movies.btn_place55.place_forget()
		Movies.btn_place56.place_forget()
		Movies.btn_place57.place_forget()
		Movies.btn_place58.place_forget()
		Movies.btn_place59.place_forget()
		Movies.btn_place60.place_forget()
		Movies.btn_place61.place_forget()
		Movies.btn_place62.place_forget()
		Movies.btn_place63.place_forget()
		Movies.btn_place64.place_forget()
		Movies.btn_place65.place_forget()
		Movies.btn_place66.place_forget()
		Movies.btn_place67.place_forget()
		Movies.btn_place68.place_forget()
		Movies.btn_place69.place_forget()
		Movies.btn_place70.place_forget()
		Movies.btn_place71.place_forget()
		Movies.btn_place72.place_forget()
		Movies.btn_place73.place_forget()
		Movies.btn_place74.place_forget()
		Movies.btn_place75.place_forget()
		Movies.btn_place76.place_forget()
		Movies.btn_place77.place_forget()
		Movies.btn_place78.place_forget()
		Movies.btn_place79.place_forget()
		Movies.btn_place80.place_forget()
		Movies.btn_place81.place_forget()
		Movies.btn_place82.place_forget()
		Movies.btn_place83.place_forget()
		Movies.btn_place84.place_forget()
		Movies.btn_place85.place_forget()
		Movies.btn_place86.place_forget()
		Movies.btn_place87.place_forget()
		Movies.btn_place88.place_forget()
		Movies.btn_place89.place_forget()
		Movies.btn_place90.place_forget()
		Movies.btn_place91.place_forget()
		Movies.btn_place92.place_forget()
		Movies.btn_place93.place_forget()
		Movies.btn_place94.place_forget()
		Movies.btn_place95.place_forget()
		Movies.btn_place96.place_forget()
		Movies.btn_place97.place_forget()
		Movies.btn_place98.place_forget()
		Movies.btn_place99.place_forget()
		Movies.btn_place100.place_forget()
		Movies.btn_place101.place_forget()
		Movies.btn_place102.place_forget()
		Movies.btn_place103.place_forget()
		Movies.btn_place104.place_forget()
		Movies.btn_place105.place_forget()
		Movies.btn_place106.place_forget()
		Movies.btn_place107.place_forget()
		Movies.btn_place108.place_forget()
		Movies.btn_place109.place_forget()
		Movies.btn_place110.place_forget()
		Movies.btn_place111.place_forget()
		Movies.btn_place112.place_forget()
		Movies.btn_place113.place_forget()
		Movies.btn_place114.place_forget()
		Movies.btn_place115.place_forget()
		Movies.btn_place116.place_forget()
		Movies.btn_place117.place_forget()
		Movies.btn_place118.place_forget()
		Movies.btn_place119.place_forget()
		Movies.btn_place120.place_forget()
		Movies.btn_place121.place_forget()
		Movies.btn_place122.place_forget()
		Movies.btn_place123.place_forget()
		Movies.btn_place124.place_forget()
		Movies.btn_place125.place_forget()
		Movies.btn_place126.place_forget()
		Movies.btn_place127.place_forget()
		Movies.btn_place128.place_forget()
		Movies.btn_place129.place_forget()
		Movies.btn_place130.place_forget()
		Movies.btn_place131.place_forget()
		Movies.btn_place132.place_forget()
		Movies.btn_place133.place_forget()
		Movies.btn_place134.place_forget()
		Movies.btn_place135.place_forget()
		Movies.btn_place136.place_forget()
		Movies.btn_place137.place_forget()
		Movies.btn_place138.place_forget()
		Movies.btn_place139.place_forget()
		Movies.btn_place140.place_forget()
		Movies.btn_place141.place_forget()
		Movies.btn_place142.place_forget()
		Movies.btn_place143.place_forget()
		Movies.btn_place144.place_forget()
		Movies.btn_place145.place_forget()
		Movies.btn_place146.place_forget()
		Movies.btn_place147.place_forget()
		Movies.btn_place148.place_forget()
		Movies.btn_place149.place_forget()
		Movies.btn_place150.place_forget()
		Movies.btn_place151.place_forget()
		Movies.btn_place152.place_forget()
		Movies.btn_place153.place_forget()
		Movies.btn_place154.place_forget()
		Movies.btn_place155.place_forget()
		Movies.btn_place156.place_forget()
		Movies.btn_place157.place_forget()
		Movies.btn_place158.place_forget()
		Movies.btn_place159.place_forget()
		Movies.btn_place160.place_forget()


	def func():
		print("Вы выполнили действие")

	def hey(arg):
		if arg == 1:
			sheet['B2'] = None
			sheet['B2'] = 1
			Movies.btn_place2 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place2.place(x=800,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 2:
			sheet['C2'] = None
			sheet['C2'] = 1
			Movies.btn_place4 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place4.place(x=1025,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 3:
			sheet['D2'] = None
			sheet['D2'] = 1
			Movies.btn_place6 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place6.place(x=1250,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 4:
			sheet['E2'] = None
			sheet['E2'] = 1
			Movies.btn_place8 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place8.place(x=1470,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 5:
			sheet['F2'] = None
			sheet['F2'] = 1
			Movies.btn_place10 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place10.place(x=1690,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 6:
			sheet['B3'] = None
			sheet['B3'] = 1
			Movies.btn_place12 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place12.place(x=800,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 7:
			sheet['C3'] = None
			sheet['C3'] = 1
			Movies.btn_place14 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place14.place(x=1025,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 8:
			sheet['D3'] = None
			sheet['D3'] = 1
			Movies.btn_place16 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place16.place(x=1250,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 9:
			sheet['E3'] = None
			sheet['E3'] = 1
			Movies.btn_place18 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place18.place(x=1470,y=520)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 10:
			sheet['F3'] = None
			sheet['F3'] = 1
			Movies.btn_place20 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place20.place(x=1690,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 11:
			sheet['B4'] = None
			sheet['B4'] = 1
			Movies.btn_place22 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place22.place(x=800,y=620)
			db.save("database.xlsx")
			Movies.func()
		elif arg == 12:
			sheet['C4'] = None
			sheet['C4'] = 1
			Movies.btn_place24 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place24.place(x=1025,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 13:
			sheet['D4'] = None
			sheet['D4'] = 1
			Movies.btn_place26 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place26.place(x=1250,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 14:
			sheet['E4'] = None
			sheet['E4'] = 1
			Movies.btn_place28 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place28.place(x=1470,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 15:
			sheet['F4'] = None
			sheet['F4'] = 1
			Movies.btn_place30 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place30.place(x=1690,y=620)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 16:
			sheet['B5'] = None
			sheet['B5'] = 1
			Movies.btn_place32 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place32.place(x=800,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 17:
			sheet['C5'] = None
			sheet['C5'] = 1
			Movies.btn_place34 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place34.place(x=1025,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 18:
			sheet['D5'] = None
			sheet['D5'] = 1
			Movies.btn_place36 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place36.place(x=1250,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 19:
			sheet['E5'] = None
			sheet['E5'] = 1
			Movies.btn_place38 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place38.place(x=1470,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 20:
			sheet['F5'] = None
			sheet['F5'] = 1
			Movies.btn_place40 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place40.place(x=1690,y=720)
			db.save('database.xlxs')
			Movies.func()

	def hey1(arg):
		if arg == 1:
			sheet['B8'] = None
			sheet['B8'] = 1
			Movies.btn_place42 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place42.place(x=800,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 2:
			sheet['C8'] = None
			sheet['C8'] = 1
			Movies.btn_place44 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place44.place(x=1025,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 3:
			sheet['D8'] = None
			sheet['D8'] = 1
			Movies.btn_place46 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place46.place(x=1250,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 4:
			sheet['E8'] = None
			sheet['E8'] = 1
			Movies.btn_place48 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place48.place(x=1470,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 5:
			sheet['F8'] = None
			sheet['F8'] = 1
			Movies.btn_place50 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place50.place(x=1690,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 6:
			sheet['B9'] = None
			sheet['B9'] = 1
			Movies.btn_place52 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place52.place(x=800,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 7:
			sheet['C9'] = None
			sheet['C9'] = 1
			Movies.btn_place54 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place54.place(x=1025,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 8:
			sheet['D9'] = None
			sheet['D9'] = 1
			Movies.btn_place56 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place56.place(x=1250,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 9:
			sheet['E9'] = None
			sheet['E9'] = 1
			Movies.btn_place58 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place58.place(x=1470,y=520)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 10:
			sheet['F9'] = None
			sheet['F9'] = 1
			Movies.btn_place60 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place60.place(x=1690,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 11:
			sheet['B10'] = None
			sheet['B10'] = 1
			Movies.btn_place62 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place62.place(x=800,y=620)
			db.save("database.xlsx")
			Movies.func()
		elif arg == 12:
			sheet['C10'] = None
			sheet['C10'] = 1
			Movies.btn_place64 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place64.place(x=1025,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 13:
			sheet['D10'] = None
			sheet['D10'] = 1
			Movies.btn_place66 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place66.place(x=1250,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 14:
			sheet['E10'] = None
			sheet['E10'] = 1
			Movies.btn_place68 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place68.place(x=1470,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 15:
			sheet['F10'] = None
			sheet['F10'] = 1
			Movies.btn_place70 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place70.place(x=1690,y=620)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 16:
			sheet['B11'] = None
			sheet['B11'] = 1
			Movies.btn_place72 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place72.place(x=800,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 17:
			sheet['C11'] = None
			sheet['C11'] = 1
			Movies.btn_place74 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place74.place(x=1025,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 18:
			sheet['D11'] = None
			sheet['D11'] = 1
			Movies.btn_place76 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place76.place(x=1250,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 19:
			sheet['E11'] = None
			sheet['E11'] = 1
			Movies.btn_place78 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place78.place(x=1470,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 20:
			sheet['F11'] = None
			sheet['F11'] = 1
			Movies.btn_place80 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place80.place(x=1690,y=720)
			db.save('database.xlxs')
			Movies.func()

	def hey2(arg):
		if arg == 1:
			sheet['I2'] = None
			sheet['I2'] = 1
			Movies.btn_place82 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place82.place(x=800,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 2:
			sheet['J2'] = None
			sheet['J2'] = 1
			Movies.btn_place84 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place84.place(x=1025,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 3:
			sheet['K2'] = None
			sheet['K2'] = 1
			Movies.btn_place86 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place86.place(x=1250,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 4:
			sheet['L2'] = None
			sheet['L2'] = 1
			Movies.btn_place88 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place88.place(x=1470,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 5:
			sheet['M2'] = None
			sheet['M2'] = 1
			Movies.btn_place90 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place90.place(x=1690,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 6:
			sheet['I3'] = None
			sheet['I3'] = 1
			Movies.btn_place92 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place92.place(x=800,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 7:
			sheet['J3'] = None
			sheet['J3'] = 1
			Movies.btn_place94 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place94.place(x=1025,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 8:
			sheet['K3'] = None
			sheet['K3'] = 1
			Movies.btn_place96 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place96.place(x=1250,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 9:
			sheet['L3'] = None
			sheet['L3'] = 1
			Movies.btn_place98 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place98.place(x=1470,y=520)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 10:
			sheet['M3'] = None
			sheet['M3'] = 1
			Movies.btn_place100 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place100.place(x=1690,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 11:
			sheet['I4'] = None
			sheet['I4'] = 1
			Movies.btn_place102 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place102.place(x=800,y=620)
			db.save("database.xlsx")
			Movies.func()
		elif arg == 12:
			sheet['J4'] = None
			sheet['J4'] = 1
			Movies.btn_place104 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place104.place(x=1025,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 13:
			sheet['K4'] = None
			sheet['K4'] = 1
			Movies.btn_place106 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place106.place(x=1250,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 14:
			sheet['L4'] = None
			sheet['L4'] = 1
			Movies.btn_place108 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place108.place(x=1470,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 15:
			sheet['M4'] = None
			sheet['M4'] = 1
			Movies.btn_place100 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place100.place(x=1690,y=620)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 16:
			sheet['I5'] = None
			sheet['I5'] = 1
			Movies.btn_place112 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place112.place(x=800,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 17:
			sheet['J5'] = None
			sheet['J5'] = 1
			Movies.btn_place114 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place114.place(x=1025,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 18:
			sheet['K5'] = None
			sheet['K5'] = 1
			Movies.btn_place116 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place116.place(x=1250,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 19:
			sheet['L5'] = None
			sheet['L5'] = 1
			Movies.btn_place118 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place118.place(x=1470,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 20:
			sheet['M5'] = None
			sheet['M5'] = 1
			Movies.btn_place120 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place120.place(x=1690,y=720)
			db.save('database.xlxs')
			Movies.func()

	def hey3(arg):
		if arg == 1:
			sheet['I8'] = None
			sheet['I8'] = 1
			Movies.btn_place122 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place122.place(x=800,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 2:
			sheet['J8'] = None
			sheet['J8'] = 1
			Movies.btn_place124 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place124.place(x=1025,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 3:
			sheet['K8'] = None
			sheet['K8'] = 1
			Movies.btn_place126 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place126.place(x=1250,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 4:
			sheet['L8'] = None
			sheet['L8'] = 1
			Movies.btn_place128 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place128.place(x=1470,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 5:
			sheet['M8'] = None
			sheet['M8'] = 1
			Movies.btn_place130 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place130.place(x=1690,y=420)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 6:
			sheet['I9'] = None
			sheet['I9'] = 1
			Movies.btn_place132 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place132.place(x=800,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 7:
			sheet['J9'] = None
			sheet['J9'] = 1
			Movies.btn_place134 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place134.place(x=1025,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 8:
			sheet['K9'] = None
			sheet['K9'] = 1
			Movies.btn_place136 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place136.place(x=1250,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 9:
			sheet['L9'] = None
			sheet['L9'] = 1
			Movies.btn_place138 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place138.place(x=1470,y=520)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 10:
			sheet['M9'] = None
			sheet['M9'] = 1
			Movies.btn_place140 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place140.place(x=1690,y=520)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 11:
			sheet['I10'] = None
			sheet['I10'] = 1
			Movies.btn_place142 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place142.place(x=800,y=620)
			db.save("database.xlsx")
			Movies.func()
		elif arg == 12:
			sheet['J10'] = None
			sheet['J10'] = 1
			Movies.btn_place144 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place144.place(x=1025,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 13:
			sheet['K10'] = None
			sheet['K10'] = 1
			Movies.btn_place146 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place146.place(x=1250,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 14:
			sheet['L10'] = None
			sheet['L10'] = 1
			Movies.btn_place148 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place148.place(x=1470,y=620)
			db.save('database.xlsx')
			Movies.func()
		elif arg == 15:
			sheet['M10'] = None
			sheet['M10'] = 1
			Movies.btn_place150 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place150.place(x=1690,y=620)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 16:
			sheet['I11'] = None
			sheet['I11'] = 1
			Movies.btn_place152 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place152.place(x=800,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 17:
			sheet['J11'] = None
			sheet['J11'] = 1
			Movies.btn_place154 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place154.place(x=1025,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 18:
			sheet['K11'] = None
			sheet['K11'] = 1
			Movies.btn_place156 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place156.place(x=1250,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 19:
			sheet['L11'] = None
			sheet['L11'] = 1
			Movies.btn_place158 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place158.place(x=1470,y=720)
			db.save('database.xlxs')
			Movies.func()
		elif arg == 20:
			sheet['M11'] = None
			sheet['M11'] = 1
			Movies.btn_place160 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
			Movies.btn_place160.place(x=1690,y=720)
			db.save('database.xlxs')
			Movies.func()


	def places():
		Movies.lbl_place.place(x=1150, y=325)
		Movies.cancel.place(x=1125,y=880)
		Movies.back.place(x=1300,y=880)
		if (sheet['B2'].value) == 0:
			Movies.btn_place1.place(x=800,y=420)
		elif (sheet['B2'].value) == 1:
			Movies.btn_place2.place(x=800,y=420)
		if (sheet['C2'].value) == 0:
			Movies.btn_place3.place(x=1025,y=420)
		elif (sheet['C2'].value) == 1:
			Movies.btn_place4.place(x=1025,y=420)
		if (sheet['D2'].value) == 0:
			Movies.btn_place5.place(x=1250,y=420)
		elif (sheet['D2'].value) == 1:
			Movies.btn_place6.place(x=1250,y=420)
		if (sheet['E2'].value) == 0:
			Movies.btn_place7.place(x=1470,y=420)
		elif (sheet['E2'].value) == 1:
			Movies.btn_place8.place(x=1470,y=420)
		if (sheet['F2'].value) == 0:
			Movies.btn_place9.place(x=1690,y=420)
		elif (sheet['F2'].value) == 1:
			Movies.btn_place10.place(x=1690,y=420)
		if (sheet['B3'].value) == 0:
			Movies.btn_place11.place(x=800,y=520)
		elif (sheet['B3'].value) == 1:
			Movies.btn_place12.place(x=800,y=520)
		if (sheet['C3'].value) == 0:
			Movies.btn_place13.place(x=1025,y=520)
		elif (sheet['C3'].value) == 1:
			Movies.btn_place14.place(x=1025,y=520)
		if (sheet['D3'].value) == 0:
			Movies.btn_place15.place(x=1250,y=520)
		elif (sheet['D3'].value) == 1:
			Movies.btn_place16.place(x=1250,y=520)
		if (sheet['E3'].value) == 0:
			Movies.btn_place17.place(x=1470,y=520)
		elif (sheet['E3'].value) == 1:
			Movies.btn_place18.place(x=1470,y=520)
		if (sheet['F3'].value) == 0:
			Movies.btn_place19.place(x=1690,y=520)
		elif (sheet['F3'].value) == 1:
			Movies.btn_place20.place(x=1690,y=520)
		if (sheet['B4'].value) == 0:
			Movies.btn_place21.place(x=800,y=620)
		elif (sheet['B4'].value) == 1:
			Movies.btn_place22.place(x=800,y=620)
		if (sheet['C4'].value) == 0:
			Movies.btn_place23.place(x=1025,y=620)
		elif (sheet['C4'].value) == 1:
			Movies.btn_place24.place(x=1025,y=620)
		if (sheet['D4'].value) == 0:
			Movies.btn_place25.place(x=1250,y=620)
		elif (sheet['D4'].value) == 1:
			Movies.btn_place26.place(x=1250,y=620)
		if (sheet['E4'].value) == 0:
			Movies.btn_place27.place(x=1470,y=620)
		elif (sheet['E4'].value) == 1:
			Movies.btn_place28.place(x=1470,y=620)
		if (sheet['F4'].value) == 0:
			Movies.btn_place29.place(x=1690,y=620)
		elif (sheet['F4'].value) == 1:
			Movies.btn_place30.place(x=1690,y=620)
		if (sheet['B5'].value) == 0:
			Movies.btn_place31.place(x=800,y=720)
		elif (sheet['B5'].value) == 1:
			Movies.btn_place32.place(x=800,y=720)
		if (sheet['C5'].value) == 0:
			Movies.btn_place33.place(x=1025,y=720)
		elif (sheet['C5'].value) == 1:
			Movies.btn_place34.place(x=1025,y=720)
		if (sheet['D5'].value) == 0:
			Movies.btn_place35.place(x=1250,y=720)
		elif (sheet['D5'].value) == 1:
			Movies.btn_place36.place(x=1250,y=720)
		if (sheet['E5'].value) == 0:
			Movies.btn_place37.place(x=1470,y=720)
		elif (sheet['E5'].value) == 1:
			Movies.btn_place38.place(x=1470,y=720)
		if (sheet['F5'].value) == 0:
			Movies.btn_place39.place(x=1690,y=720)
		elif (sheet['F5'].value) == 1:
			Movies.btn_place40.place(x=1690,y=720)

	def places1():
		Movies.lbl_place.place(x=1150, y=325)
		Movies.cancel.place(x=1125,y=880)
		Movies.back.place(x=1300, y=880)
		if (sheet['B8'].value) == 0:
			Movies.btn_place41.place(x=800,y=420)
		elif (sheet['B8'].value) == 1:
			Movies.btn_place42.place(x=800,y=420)
		if (sheet['C8'].value) == 0:
			Movies.btn_place43.place(x=1025,y=420)
		elif (sheet['C8'].value) == 1:
			Movies.btn_place44.place(x=1025,y=420)
		if (sheet['D8'].value) == 0:
			Movies.btn_place45.place(x=1250,y=420)
		elif (sheet['D8'].value) == 1:
			Movies.btn_place46.place(x=1250,y=420)
		if (sheet['E8'].value) == 0:
			Movies.btn_place47.place(x=1470,y=420)
		elif (sheet['E8'].value) == 1:
			Movies.btn_place48.place(x=1470,y=420)
		if (sheet['F8'].value) == 0:
			Movies.btn_place49.place(x=1690,y=420)
		elif (sheet['F8'].value) == 1:
			Movies.btn_place50.place(x=1690,y=420)
		if (sheet['B9'].value) == 0:
			Movies.btn_place51.place(x=800,y=520)
		elif (sheet['B9'].value) == 1:
			Movies.btn_place52.place(x=800,y=520)
		if (sheet['C9'].value) == 0:
			Movies.btn_place53.place(x=1025,y=520)
		elif (sheet['C9'].value) == 1:
			Movies.btn_place54.place(x=1025,y=520)
		if (sheet['D9'].value) == 0:
			Movies.btn_place55.place(x=1250,y=520)
		elif (sheet['D9'].value) == 1:
			Movies.btn_place56.place(x=1250,y=520)
		if (sheet['E9'].value) == 0:
			Movies.btn_place57.place(x=1470,y=520)
		elif (sheet['E9'].value) == 1:
			Movies.btn_place58.place(x=1470,y=520)
		if (sheet['F9'].value) == 0:
			Movies.btn_place59.place(x=1690,y=520)
		elif (sheet['F9'].value) == 1:
			Movies.btn_place60.place(x=1690,y=520)
		if (sheet['B10'].value) == 0:
			Movies.btn_place61.place(x=800,y=620)
		elif (sheet['B10'].value) == 1:
			Movies.btn_place62.place(x=800,y=620)
		if (sheet['C10'].value) == 0:
			Movies.btn_place63.place(x=1025,y=620)
		elif (sheet['C10'].value) == 1:
			Movies.btn_place64.place(x=1025,y=620)
		if (sheet['D10'].value) == 0:
			Movies.btn_place65.place(x=1250,y=620)
		elif (sheet['D10'].value) == 1:
			Movies.btn_place66.place(x=1250,y=620)
		if (sheet['E10'].value) == 0:
			Movies.btn_place67.place(x=1470,y=620)
		elif (sheet['E10'].value) == 1:
			Movies.btn_place68.place(x=1470,y=620)
		if (sheet['F10'].value) == 0:
			Movies.btn_place69.place(x=1690,y=620)
		elif (sheet['F10'].value) == 1:
			Movies.btn_place70.place(x=1690,y=620)
		if (sheet['B11'].value) == 0:
			Movies.btn_place71.place(x=800,y=720)
		elif (sheet['B11'].value) == 1:
			Movies.btn_place72.place(x=800,y=720)
		if (sheet['C11'].value) == 0:
			Movies.btn_place73.place(x=1025,y=720)
		elif (sheet['C11'].value) == 1:
			Movies.btn_place74.place(x=1025,y=720)
		if (sheet['D11'].value) == 0:
			Movies.btn_place75.place(x=1250,y=720)
		elif (sheet['D11'].value) == 1:
			Movies.btn_place76.place(x=1250,y=720)
		if (sheet['E11'].value) == 0:
			Movies.btn_place77.place(x=1470,y=720)
		elif (sheet['E11'].value) == 1:
			Movies.btn_place78.place(x=1470,y=720)
		if (sheet['F11'].value) == 0:
			Movies.btn_place79.place(x=1690,y=720)
		elif (sheet['F11'].value) == 1:
			Movies.btn_place80.place(x=1690,y=720)

	def places2():
		Movies.lbl_place.place(x=1150, y=325)
		Movies.cancel.place(x=1125,y=880)
		Movies.back.place(x=1300, y=880)
		if (sheet['I2'].value) == 0:
			Movies.btn_place81.place(x=800,y=420)
		elif (sheet['I2'].value) == 1:
			Movies.btn_place82.place(x=800,y=420)
		if (sheet['J2'].value) == 0:
			Movies.btn_place83.place(x=1025,y=420)
		elif (sheet['J2'].value) == 1:
			Movies.btn_place84.place(x=1025,y=420)
		if (sheet['K2'].value) == 0:
			Movies.btn_place85.place(x=1250,y=420)
		elif (sheet['K2'].value) == 1:
			Movies.btn_place86.place(x=1250,y=420)
		if (sheet['L2'].value) == 0:
			Movies.btn_place87.place(x=1470,y=420)
		elif (sheet['L2'].value) == 1:
			Movies.btn_place88.place(x=1470,y=420)
		if (sheet['M2'].value) == 0:
			Movies.btn_place89.place(x=1690,y=420)
		elif (sheet['M2'].value) == 1:
			Movies.btn_place90.place(x=1690,y=420)
		if (sheet['I3'].value) == 0:
			Movies.btn_place91.place(x=800,y=520)
		elif (sheet['I3'].value) == 1:
			Movies.btn_place92.place(x=800,y=520)
		if (sheet['J3'].value) == 0:
			Movies.btn_place93.place(x=1025,y=520)
		elif (sheet['J3'].value) == 1:
			Movies.btn_place94.place(x=1025,y=520)
		if (sheet['K3'].value) == 0:
			Movies.btn_place95.place(x=1250,y=520)
		elif (sheet['K3'].value) == 1:
			Movies.btn_place96.place(x=1250,y=520)
		if (sheet['L3'].value) == 0:
			Movies.btn_place97.place(x=1470,y=520)
		elif (sheet['L3'].value) == 1:
			Movies.btn_place98.place(x=1470,y=520)
		if (sheet['M3'].value) == 0:
			Movies.btn_place99.place(x=1690,y=520)
		elif (sheet['M3'].value) == 1:
			Movies.btn_place100.place(x=1690,y=520)
		if (sheet['I4'].value) == 0:
			Movies.btn_place101.place(x=800,y=620)
		elif (sheet['I4'].value) == 1:
			Movies.btn_place102.place(x=800,y=620)
		if (sheet['J4'].value) == 0:
			Movies.btn_place103.place(x=1025,y=620)
		elif (sheet['J4'].value) == 1:
			Movies.btn_place104.place(x=1025,y=620)
		if (sheet['K4'].value) == 0:
			Movies.btn_place105.place(x=1250,y=620)
		elif (sheet['K4'].value) == 1:
			Movies.btn_place106.place(x=1250,y=620)
		if (sheet['L4'].value) == 0:
			Movies.btn_place107.place(x=1470,y=620)
		elif (sheet['L4'].value) == 1:
			Movies.btn_place108.place(x=1470,y=620)
		if (sheet['M4'].value) == 0:
			Movies.btn_place109.place(x=1690,y=620)
		elif (sheet['M4'].value) == 1:
			Movies.btn_place110.place(x=1690,y=620)
		if (sheet['I5'].value) == 0:
			Movies.btn_place111.place(x=800,y=720)
		elif (sheet['I5'].value) == 1:
			Movies.btn_place112.place(x=800,y=720)
		if (sheet['J5'].value) == 0:
			Movies.btn_place113.place(x=1025,y=720)
		elif (sheet['J5'].value) == 1:
			Movies.btn_place114.place(x=1025,y=720)
		if (sheet['K5'].value) == 0:
			Movies.btn_place115.place(x=1250,y=720)
		elif (sheet['K5'].value) == 1:
			Movies.btn_place116.place(x=1250,y=720)
		if (sheet['L5'].value) == 0:
			Movies.btn_place117.place(x=1470,y=720)
		elif (sheet['L5'].value) == 1:
			Movies.btn_place118.place(x=1470,y=720)
		if (sheet['M5'].value) == 0:
			Movies.btn_place119.place(x=1690,y=720)
		elif (sheet['M5'].value) == 1:
			Movies.btn_place120.place(x=1690,y=720)

	def places3():
		Movies.lbl_place.place(x=1150, y=325)
		Movies.cancel.place(x=1125,y=880)
		Movies.back.place(x=1300, y=880)
		if (sheet['I8'].value) == 0:
			Movies.btn_place121.place(x=800,y=420)
		elif (sheet['I8'].value) == 1:
			Movies.btn_place122.place(x=800,y=420)
		if (sheet['J8'].value) == 0:
			Movies.btn_place123.place(x=1025,y=420)
		elif (sheet['J8'].value) == 1:
			Movies.btn_place124.place(x=1025,y=420)
		if (sheet['K8'].value) == 0:
			Movies.btn_place125.place(x=1250,y=420)
		elif (sheet['K8'].value) == 1:
			Movies.btn_place126.place(x=1250,y=420)
		if (sheet['L8'].value) == 0:
			Movies.btn_place127.place(x=1470,y=420)
		elif (sheet['L8'].value) == 1:
			Movies.btn_place128.place(x=1470,y=420)
		if (sheet['M8'].value) == 0:
			Movies.btn_place129.place(x=1690,y=420)
		elif (sheet['M8'].value) == 1:
			Movies.btn_place130.place(x=1690,y=420)
		if (sheet['I9'].value) == 0:
			Movies.btn_place131.place(x=800,y=520)
		elif (sheet['I9'].value) == 1:
			Movies.btn_place132.place(x=800,y=520)
		if (sheet['J9'].value) == 0:
			Movies.btn_place133.place(x=1025,y=520)
		elif (sheet['J9'].value) == 1:
			Movies.btn_place134.place(x=1025,y=520)
		if (sheet['K9'].value) == 0:
			Movies.btn_place135.place(x=1250,y=520)
		elif (sheet['K9'].value) == 1:
			Movies.btn_place136.place(x=1250,y=520)
		if (sheet['L9'].value) == 0:
			Movies.btn_place137.place(x=1470,y=520)
		elif (sheet['L9'].value) == 1:
			Movies.btn_place138.place(x=1470,y=520)
		if (sheet['M9'].value) == 0:
			Movies.btn_place139.place(x=1690,y=520)
		elif (sheet['M9'].value) == 1:
			Movies.btn_place140.place(x=1690,y=520)
		if (sheet['I10'].value) == 0:
			Movies.btn_place141.place(x=800,y=620)
		elif (sheet['I10'].value) == 1:
			Movies.btn_place142.place(x=800,y=620)
		if (sheet['J10'].value) == 0:
			Movies.btn_place143.place(x=1025,y=620)
		elif (sheet['J10'].value) == 1:
			Movies.btn_place144.place(x=1025,y=620)
		if (sheet['K10'].value) == 0:
			Movies.btn_place145.place(x=1250,y=620)
		elif (sheet['K10'].value) == 1:
			Movies.btn_place146.place(x=1250,y=620)
		if (sheet['L10'].value) == 0:
			Movies.btn_place147.place(x=1470,y=620)
		elif (sheet['L10'].value) == 1:
			Movies.btn_place148.place(x=1470,y=620)
		if (sheet['M10'].value) == 0:
			Movies.btn_place149.place(x=1690,y=620)
		elif (sheet['M10'].value) == 1:
			Movies.btn_place150.place(x=1690,y=620)
		if (sheet['I11'].value) == 0:
			Movies.btn_place151.place(x=800,y=720)
		elif (sheet['I11'].value) == 1:
			Movies.btn_place152.place(x=800,y=720)
		if (sheet['J11'].value) == 0:
			Movies.btn_place153.place(x=1025,y=720)
		elif (sheet['J11'].value) == 1:
			Movies.btn_place154.place(x=1025,y=720)
		if (sheet['K11'].value) == 0:
			Movies.btn_place155.place(x=1250,y=720)
		elif (sheet['K11'].value) == 1:
			Movies.btn_place156.place(x=1250,y=720)
		if (sheet['L11'].value) == 0:
			Movies.btn_place157.place(x=1470,y=720)
		elif (sheet['L11'].value) == 1:
			Movies.btn_place158.place(x=1470,y=720)
		if (sheet['M11'].value) == 0:
			Movies.btn_place159.place(x=1690,y=720)
		elif (sheet['M11'].value) == 1:
			Movies.btn_place160.place(x=1690,y=720)

	def obvodka(arg):
		if arg == 1:
			Movies.box.itemconfig('2a', fill="azure3")
			Movies.box.itemconfig('3a', fill="azure3")
			Movies.box.itemconfig('4a', fill="azure3")
			Movies.box.create_line(58,118,270,118, fill="red", width=5, tag="1a")
			Movies.box.create_line(58,118,58,396, fill="red", width=5, tag="1a")
			Movies.box.create_line(58,396,270,396, fill="red", width=5, tag="1a")
			Movies.box.create_line(268,396,268,118, fill="red", width=5, tag="1a")
			Movies.kinozal_rdbtn1.place(x=750, y=50)
			Movies.kinozal_rdbtn2.place(x=1180, y=50)
			Movies.kinozal_rdbtn3.place(x=1600, y=50)
			Movies.func()
		elif arg == 2:
			Movies.box.itemconfig('1a', fill="azure3")
			Movies.box.itemconfig('4a', fill="azure3")
			Movies.box.itemconfig('3a', fill="azure3")
			Movies.box.create_line(359,118,569,118, fill="red", width=5, tag="2a")
			Movies.box.create_line(358,118,358,396, fill="red", width=5, tag="2a")
			Movies.box.create_line(359,396,569,396, fill="red", width=5, tag="2a")
			Movies.box.create_line(569,396,569,118, fill="red", width=5, tag="2a")
			Movies.kinozal_rdbtn4.place(x=750, y=50)
			Movies.kinozal_rdbtn5.place(x=1180, y=50)
			Movies.kinozal_rdbtn6.place(x=1600, y=50)
			Movies.func()
		elif arg == 3:
			Movies.box.itemconfig('2a', fill="azure3")
			Movies.box.itemconfig('1a', fill="azure3")
			Movies.box.itemconfig('4a', fill="azure3")
			Movies.box.create_line(58,396,270,396, fill="red", width=5, tag="3a")
			Movies.box.create_line(58,396,58,676, fill="red", width=5, tag="3a")
			Movies.box.create_line(58,676,270,676, fill="red", width=5, tag="3a")
			Movies.box.create_line(270,676,270,396, fill="red", width=5, tag="3a")
			Movies.kinozal_rdbtn7.place(x=750, y=50)
			Movies.kinozal_rdbtn8.place(x=1180, y=50)
			Movies.kinozal_rdbtn9.place(x=1600, y=50)
			Movies.func()
		elif arg == 4:
			Movies.box.itemconfig('2a', fill="azure3")
			Movies.box.itemconfig('3a', fill="azure3")
			Movies.box.itemconfig('1a', fill="azure3")
			Movies.box.create_line(359,396,569,396, fill="red", width=5, tag="4a")
			Movies.box.create_line(357,396,357,676, fill="red", width=5, tag="4a")
			Movies.box.create_line(357,676,569,676, fill="red", width=5, tag="4a")
			Movies.box.create_line(569,676,569,396, fill="red", width=5, tag="4a")
			Movies.kinozal_rdbtn10.place(x=750, y=50)
			Movies.kinozal_rdbtn11.place(x=1180, y=50)
			Movies.kinozal_rdbtn12.place(x=1600, y=50)
			Movies.func()


	def check_answer():
		if var.get() == 1:
			Movies.btn_time3.place_forget()
			Movies.btn_time4.place_forget()
			Movies.btn_time5.place_forget()
			Movies.btn_time6.place_forget()
			Movies.btn_time1.place(x=850, y=160)
			Movies.btn_time2.place(x=1400, y=160)
		elif var.get() == 2:
			Movies.btn_time1.place_forget()
			Movies.btn_time2.place_forget()
			Movies.btn_time5.place_forget()
			Movies.btn_time6.place_forget()
			Movies.btn_time3.place(x=850, y=160)
			Movies.btn_time4.place(x=1400, y=160)
		elif var.get() == 3:
			Movies.btn_time1.place_forget()
			Movies.btn_time2.place_forget()
			Movies.btn_time3.place_forget()
			Movies.btn_time4.place_forget()
			Movies.btn_time5.place(x=850, y=160)
			Movies.btn_time6.place(x=1400, y=160)



	def change_poster(arg):
		if arg == 1:
			Movies.b1.config(image=Movies.photo11)
			(sheet['B1'].value) = None
			(sheet['B1'].value) = "Новый фильм"
			db.save('database.xlsx')
			Movies.func()
		elif arg == 2:
			Movies.b1.config(image=Movies.photo1)
			(sheet['B1'].value) = None
			(sheet['B1'].value) = "Бэтмен"
			db.save('database.xlsx')
			Movies.func()
		if arg == 3:
			Movies.b2.config(image=Movies.photo21)
			(sheet['A14'].value) = None
			(sheet['A14'].value) = "Фильм прометей"
			db.save('database.xlsx')
			Movies.func()
		elif arg == 4:
			Movies.b2.config(image=Movies.photo2)
			(sheet['A14'].value) = None
			(sheet['A14'].value) = "Фильм Чудо-женщина"
			db.save('database.xlsx')
			Movies.func()
		if arg == 5:
			Movies.b3.config(image=Movies.photo31)
			(sheet['A28'].value) = None
			(sheet['A28'].value) = "Фильм Марсианин"
			db.save('database.xlsx')
			Movies.func()
		elif arg == 6:
			Movies.b3.config(image=Movies.photo3)
			(sheet['A28'].value) = None
			(sheet['A28'].value) = "Фильм На игре"
			db.save('database.xlsx')
			Movies.func()
		if arg == 7:
			Movies.b4.config(image=Movies.photo41)
			(sheet['A42'].value) = None
			(sheet['A42'].value) = "Фильм batman"
			db.save('database.xlsx')
			Movies.func()
		elif arg == 8:
			Movies.b4.config(image=Movies.photo4)
			(sheet['A42'].value) = None
			(sheet['A42'].value) = "Фильм X-men"
			db.save('database.xlsx')
			Movies.func()



	box = Canvas(window, width = 1920, height=1080, bg="azure3") 
	box.pack(side=LEFT)
	b1 = Button(box, command =lambda: Movies.obvodka(1))
	b2 = Button(box, command =lambda: Movies.obvodka(2))
	b3 = Button(box, command =lambda: Movies.obvodka(3))
	b4 = Button(box, command =lambda: Movies.obvodka(4))
	b1.place(x=60,y=120)
	b2.place(x=360,y=120)
	b3.place(x=60,y=400)
	b4.place(x=360,y=400)
	image1 = Image.open("batman.png")
	photo1 = ImageTk.PhotoImage(image1)
	image2 = Image.open("women.png")
	photo2 = ImageTk.PhotoImage(image2)
	image3 = Image.open("naigre.png")
	photo3 = ImageTk.PhotoImage(image3)
	image4 = Image.open("xmen.png")
	photo4 = ImageTk.PhotoImage(image4)
	image11 = Image.open("oxotniki.png")
	photo11 = ImageTk.PhotoImage(image11)
	image21 = Image.open("prometei.png")
	photo21 = ImageTk.PhotoImage(image21)
	image31 = Image.open("mars.png")
	photo31 = ImageTk.PhotoImage(image31)
	image41 = Image.open("batman.png")
	photo41 = ImageTk.PhotoImage(image41)
	b1.config(image=photo1)
	b2.config(image=photo2)
	b3.config(image=photo3)
	b4.config(image=photo4)
	seansi = Label(box, text="Сеансы на сегодня", bg="azure3", font=("Arial", 30))
	seansi.place(x=140, y=50)
	next1 = Button(box, text="-->", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(1))
	prev1 = Button(box, text="<--", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(2))
	next2 = Button(box, text="-->", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(3))
	prev2 = Button(box, text="<--", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(4))
	next3 = Button(box, text="-->", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(5))
	prev3 = Button(box, text="<--", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(6))
	next4 = Button(box, text="-->", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(7))
	prev4 = Button(box, text="<--", bg="white", font=("Arial", 10), command=lambda: Movies.change_poster(8))
	next1.place(x=275,y=240)
	prev1.place(x=25,y=240)
	next2.place(x=575,y=240)
	prev2.place(x=325,y=240)
	next3.place(x=275,y=540)
	prev3.place(x=25,y=540)
	next4.place(x=575,y=540)
	prev4.place(x=325,y=540)
	btn_time1 = Button(text=(sheet['A2'].value), font=("Arial", 30), bg="azure3", command=places)
	btn_time2 = Button(text=(sheet['A8'].value), font=("Arial", 30), bg="azure3", command=places1)
	btn_time3 = Button(text=(sheet['H2'].value), font=("Arial", 30), bg="azure3", command=places2)
	btn_time4 = Button(text=(sheet['H8'].value), font=("Arial", 30), bg="azure3", command=places3)
	btn_time5 = Button(text=(sheet['O2'].value), font=("Arial", 30), bg="azure3",)
	btn_time6 = Button(text=(sheet['O8'].value), font=("Arial", 30), bg="azure3",)
	btn_place1 = Button(text="1.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(1))
	btn_place2 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place3 = Button(text="1.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(2))
	btn_place4 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place5 = Button(text="1.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(3))
	btn_place6 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place7 = Button(text="1.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(4))
	btn_place8 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place9 = Button(text="1.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(5))
	btn_place10 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place11 = Button(text="2.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(6))
	btn_place12 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place13 = Button(text="2.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(7))
	btn_place14 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place15 = Button(text="2.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(8))
	btn_place16 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place17 = Button(text="2.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(9))
	btn_place18 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place19 = Button(text="2.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(10))
	btn_place20 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place21 = Button(text="3.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(11))
	btn_place22 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place23 = Button(text="3.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(12))
	btn_place24 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place25 = Button(text="3.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(13))
	btn_place26 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place27 = Button(text="3.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(14))
	btn_place28 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place29 = Button(text="3.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(15))
	btn_place30 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place31 = Button(text="4.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(16))
	btn_place32 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place33 = Button(text="4.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(17))
	btn_place34 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place35 = Button(text="4.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(18))
	btn_place36 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place37 = Button(text="4.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(19))
	btn_place38 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place39 = Button(text="4.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey(20))
	btn_place40 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place41 = Button(text="1.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(1))
	btn_place42 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place43 = Button(text="1.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(2))
	btn_place44 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place45 = Button(text="1.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(3))
	btn_place46 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place47 = Button(text="1.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(4))
	btn_place48 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place49 = Button(text="1.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(5))
	btn_place50 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place51 = Button(text="2.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(6))
	btn_place52 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place53 = Button(text="2.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(7))
	btn_place54 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place55 = Button(text="2.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(8))
	btn_place56 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place57 = Button(text="2.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(9))
	btn_place58 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place59 = Button(text="2.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(10))
	btn_place60 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place61 = Button(text="3.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(11))
	btn_place62 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place63 = Button(text="3.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(12))
	btn_place64 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place65 = Button(text="3.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(13))
	btn_place66 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place67 = Button(text="3.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(14))
	btn_place68 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place69 = Button(text="3.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(15))
	btn_place70 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place71 = Button(text="4.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(16))
	btn_place72 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place73 = Button(text="4.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(17))
	btn_place74 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place75 = Button(text="4.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(18))
	btn_place76 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place77 = Button(text="4.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(19))
	btn_place78 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place79 = Button(text="4.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey1(20))
	btn_place80 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place81 = Button(text="1.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(1))
	btn_place82 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place83 = Button(text="1.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(2))
	btn_place84 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place85 = Button(text="1.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(3))
	btn_place86 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place87 = Button(text="1.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(4))
	btn_place88 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place89 = Button(text="1.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(5))
	btn_place90 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place91 = Button(text="2.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(6))
	btn_place92 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place93 = Button(text="2.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(7))
	btn_place94 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place95 = Button(text="2.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(8))
	btn_place96 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place97 = Button(text="2.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(9))
	btn_place98 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place99 = Button(text="2.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(10))
	btn_place100 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place101 = Button(text="3.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(11))
	btn_place102 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place103 = Button(text="3.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(12))
	btn_place104 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place105 = Button(text="3.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(13))
	btn_place106 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place107 = Button(text="3.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(14))
	btn_place108 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place109 = Button(text="3.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(15))
	btn_place110 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place111 = Button(text="4.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(16))
	btn_place112 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place113 = Button(text="4.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(17))
	btn_place114 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place115 = Button(text="4.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(18))
	btn_place116 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place117 = Button(text="4.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(19))
	btn_place118 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place119 = Button(text="4.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey2(20))
	btn_place120 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place121 = Button(text="1.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(1))
	btn_place122 = Button(text="1.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place123 = Button(text="1.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(2))
	btn_place124 = Button(text="1.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place125 = Button(text="1.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(3))
	btn_place126 = Button(text="1.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place127 = Button(text="1.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(4))
	btn_place128 = Button(text="1.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place129 = Button(text="1.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(5))
	btn_place130 = Button(text="1.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place131 = Button(text="2.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(6))
	btn_place132 = Button(text="2.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place133 = Button(text="2.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(7))
	btn_place134 = Button(text="2.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place135 = Button(text="2.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(8))
	btn_place136 = Button(text="2.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place137 = Button(text="2.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(9))
	btn_place138 = Button(text="2.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place139 = Button(text="2.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(10))
	btn_place140 = Button(text="2.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place141 = Button(text="3.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(11))
	btn_place142 = Button(text="3.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place143 = Button(text="3.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(12))
	btn_place144 = Button(text="3.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place145 = Button(text="3.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(13))
	btn_place146 = Button(text="3.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place147 = Button(text="3.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(14))
	btn_place148 = Button(text="3.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place149 = Button(text="3.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(15))
	btn_place150 = Button(text="3.5", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place151 = Button(text="4.1", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(16))
	btn_place152 = Button(text="4.1", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place153 = Button(text="4.2", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(17))
	btn_place154 = Button(text="4.2", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place155 = Button(text="4.3", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(18))
	btn_place156 = Button(text="4.3", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place157 = Button(text="4.4", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(19))
	btn_place158 = Button(text="4.4", height=2, width=8, bg='red', font=("Arial", 20))
	btn_place159 = Button(text="4.5", height=2, width=8, bg='green', font=("Arial", 20), command=lambda: Movies.hey3(20))
	btn_place160 = Button(text="4.5", height=2, width=8, bg='red', font=("Arial", 20))
	kinozal_rdbtn1 = Radiobutton(text="Кинозал 1", variable=var, value=1, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn2 = Radiobutton(text="Кинозал 2", variable=var, value=2, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn3 = Radiobutton(text="Кинозал 3", variable=var, value=3, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn4 = Radiobutton(text="Кинозал 1", variable=var, value=4, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn5 = Radiobutton(text="Кинозал 2", variable=var, value=5, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn6 = Radiobutton(text="Кинозал 3", variable=var, value=6, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn7 = Radiobutton(text="Кинозал 1", variable=var, value=7, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn8 = Radiobutton(text="Кинозал 2", variable=var, value=8, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn9 = Radiobutton(text="Кинозал 3", variable=var, value=9, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn10 = Radiobutton(text="Кинозал 1", variable=var, value=10, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn11 = Radiobutton(text="Кинозал 2", variable=var, value=11, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn12 = Radiobutton(text="Кинозал 3", variable=var, value=12, style = 'Wild.TRadiobutton', command=check_answer)
	cancel = Button(text="К фильмам", width=10, bg="azure3", font=("Arial", 20), command=cancel)
	back = Button(text="Назад", width=8, bg="azure3", font=("Arial", 20), command=back)
	lbl_place = Label(box, text="Выберите места", bg="azure3", font=("Arial", 30))



class Razmetka1():
	Movies.box.create_line(700,0,700,1080, fill="black", tag="lines", width=3)
	Movies.box.create_line(0,110,1920,110, fill="black", tag="lines", width=3)
	Movies.box.create_line(700,300,1920,300, fill="black", tag="lines", width=3)
	Movies.box.create_line(750, 400, 1870, 400, fill="black", tag="lines", width=3)
	Movies.box.create_line(750, 400, 750, 1000, fill="black", tag="lines", width=3)
	Movies.box.create_line(750, 1000, 1870, 1000, fill="black", tag="lines", width=3)
	Movies.box.create_line(1870, 1000, 1870, 400, fill="black", tag="lines", width=3)
	Movies.box.create_line(0,800,700,800, fill="black", tag="lines", width=3)

def timing():
	#display current hour,minute,seconds
	current_time = time.strftime("%H : %M : %S")
	clock.config(text=current_time)
	#clock will change after every 200 microseconds
	clock.after(200,timing)

clock = Label(Movies.box,font=("times",30,"bold"),bg="azure3")
clock.place(x=250,y=970)
today = Label(Movies.box,font=("times",30,"bold"),bg="azure3")
today.config(text=date)
today.place(x=250, y=870)
timing()


if __name__ == "__main__":
	Vid = View()
	Movie = Movies()
	Raz = Razmetka1()
	app = Panel() 
	timing()     
	window.mainloop()