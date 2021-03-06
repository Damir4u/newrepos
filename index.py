from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Radiobutton  
import tkinter.ttk as ttk
import openpyxl
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

class View():
	white_color = "white"
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

		def change_view():
			if fon.get() == 1:
				Movies.box['bg'] = "white"
				Movies.box.itemconfig('obvodka', fill="red")
				Movies.box.itemconfig('lines',fill="black")
				View.s.configure('Wild.TRadiobutton', background=View.white_color, foreground="black")
			elif fon.get() == 2:
				Movies.box['bg'] = "#333333" 
				Movies.box.itemconfig('obvodka', fill="#33FF33")
				Movies.box.itemconfig('lines',fill="white")
				View.s1.configure('Wild.TRadiobutton', background=View.black_color, foreground="white")
		menu = Menu(window)
		file_menu = Menu(menu, tearoff=0)
		view = Menu(menu, tearoff=0)
		spravka = Menu(menu, tearoff=0)

		file_menu.add_command(label="Билеты")
		file_menu.add_command(label="Фильмы")
		file_menu.add_command(label="Залы")

		view.add_radiobutton(label="Светлый режим", variable=fon, value= 1, command=change_view)
		view.add_radiobutton(label="Темный режим", variable=fon, value= 2, command=change_view)

		spravka.add_command(label="Просмотреть справку",)
		spravka.add_separator()
		spravka.add_command(label="О программе", command=about_programm)

		menu.add_cascade(label="Данные", menu=file_menu)
		menu.add_cascade(label="Вид", menu=view)
		menu.add_cascade(label="Справка", menu=spravka)
		menu.add_command(label="Выход", command=window.destroy)
		window.config(menu=menu)

class Movies():

	def cancel():
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

	def func():
		print("Вы выбрали место")

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


	def places():
		Movies.lbl_place.place(x=1150, y=325)
		Movies.cancel.place(x=1250,y=880)
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
		Movies.cancel.place(x=1250,y=880)
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

	def obvodka():
		Movies.box.create_line(58,118,270,118, fill="red", width=5, tag="obvodka")
		Movies.box.create_line(58,118,58,396, fill="red", width=5, tag="obvodka")
		Movies.box.create_line(58,396,270,396, fill="red", width=5, tag="obvodka")
		Movies.box.create_line(268,396,268,118, fill="red", width=5, tag="obvodka")
		Movies.kinozal_rdbtn1.place(x=750, y=50)
		Movies.kinozal_rdbtn2.place(x=1150, y=50)
		Movies.kinozal_rdbtn3.place(x=1600, y=50)

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


	box = Canvas(window, width = 1920, height=1080, bg="white") 
	box.pack(side=LEFT)
	b1 = Button(box, command = obvodka)
	b2 = Button(box)
	b3 = Button(box)
	b4 = Button(box)
	b5 = Button(box)
	b6 = Button(box)
	b1.place(x=60,y=120)
	b2.place(x=360,y=120)
	b3.place(x=60,y=400)
	b4.place(x=360,y=400)
	b5.place(x=60,y=680)
	b6.place(x=360,y=680)
	image1 = Image.open("batman.png")
	photo1 = ImageTk.PhotoImage(image1)
	image2 = Image.open("women.png")
	photo2 = ImageTk.PhotoImage(image2)
	image3 = Image.open("naigre.png")
	photo3 = ImageTk.PhotoImage(image3)
	image4 = Image.open("xmen.png")
	photo4 = ImageTk.PhotoImage(image4)
	image5 = Image.open("mars.png")
	photo5 = ImageTk.PhotoImage(image5)
	image6 = Image.open("prometei.png")
	photo6 = ImageTk.PhotoImage(image6)
	b1.config(image=photo1)
	b2.config(image=photo2)
	b3.config(image=photo3)
	b4.config(image=photo4)
	b5.config(image=photo5)
	b6.config(image=photo6)
	seansi = Label(box, text="Сеансы на сегодня", bg="white", font=("Arial", 30))
	seansi.place(x=140, y=50)
	btn_time1 = Button(text=(sheet['A2'].value), font=("Arial", 30), command=places)
	btn_time2 = Button(text=(sheet['A8'].value), font=("Arial", 30), command=places1)
	btn_time3 = Button(text=(sheet['H2'].value), font=("Arial", 30))
	btn_time4 = Button(text=(sheet['H8'].value), font=("Arial", 30))
	btn_time5 = Button(text=(sheet['O2'].value), font=("Arial", 30))
	btn_time6 = Button(text=(sheet['O8'].value), font=("Arial", 30))
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
	kinozal_rdbtn1 = Radiobutton(text="Кинозал 1", variable=var, value=1, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn2 = Radiobutton(text="Кинозал 2", variable=var, value=2, style = 'Wild.TRadiobutton', command=check_answer)
	kinozal_rdbtn3 = Radiobutton(text="Кинозал 3", variable=var, value=3, style = 'Wild.TRadiobutton', command=check_answer)
	cancel = Button(text="Назад", width=8, bg='white', font=("Arial", 20), command=cancel)
	lbl_place = Label(box, text="Выберите места", bg="white", font=("Arial", 30))

class Razmetka1():
	Movies.box.create_line(700,0,700,1080, fill="black", tag="lines")
	Movies.box.create_line(0,110,1920,110, fill="black", tag="lines")
	Movies.box.create_line(700,300,1920,300, fill="black", tag="lines")
	Movies.box.create_line(750, 400, 1870, 400, fill="black", tag="lines")
	Movies.box.create_line(750, 400, 750, 1000, fill="black", tag="lines")
	Movies.box.create_line(750, 1000, 1870, 1000, fill="black", tag="lines")
	Movies.box.create_line(1870, 1000, 1870, 400, fill="black", tag="lines")



if __name__ == "__main__":
	Vid = View()
	Movie = Movies()
	Raz = Razmetka1()
	app = Panel()      
	window.mainloop()