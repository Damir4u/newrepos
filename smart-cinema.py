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
boss_menu = window
db = openpyxl.load_workbook('database.xlsx')
sheets = db.sheetnames
sheet = db.active
white_color = "white"
black_color = "#333333"
window.configure(bg=white_color)
window.configure(bg=black_color)
s = ttk.Style()
s1 = ttk.Style()
var = IntVar()
var.set(0)
s.configure('Wild.TRadiobutton', background=white_color, foreground="black", width="9", height="20", font=("Arial", 40))

def back():
    kinozal_rdbtn1.place_forget()
    kinozal_rdbtn2.place_forget()
    kinozal_rdbtn3.place_forget()
    btn_delete_places.place_forget()
    btn_time1.place_forget()
    btn_time2.place_forget()
    btn_time3.place_forget()
    btn_time4.place_forget()
    btn_time5.place_forget()
    btn_time6.place_forget()
    btn_place1.place_forget()
    btn_place2.place_forget()
    btn_place3.place_forget()
    btn_place4.place_forget()
    btn_place5.place_forget()
    btn_place6.place_forget()
    btn_place7.place_forget()
    btn_place8.place_forget()
    btn_place9.place_forget()
    btn_place10.place_forget()
    btn_place11.place_forget()
    btn_place12.place_forget()
    btn_place13.place_forget()
    btn_place14.place_forget()
    btn_place15.place_forget()
    btn_place16.place_forget()
    btn_place17.place_forget()
    btn_place18.place_forget()
    btn_place19.place_forget()
    btn_place20.place_forget()
    btn_delete_places.place_forget()
    btn_back.destroy()


def back1():
    kinozal_rdbtn1.place_forget()
    kinozal_rdbtn2.place_forget()
    kinozal_rdbtn3.place_forget()
    btn_time1.place_forget()
    btn_time2.place_forget()
    btn_time3.place_forget()
    btn_time4.place_forget()
    btn_time5.place_forget()
    btn_time6.place_forget()
    btn_place21.place_forget()
    btn_place22.place_forget()
    btn_place23.place_forget()
    btn_place24.place_forget()
    btn_place25.place_forget()
    btn_place26.place_forget()
    btn_place27.place_forget()
    btn_place28.place_forget()
    btn_place29.place_forget()
    btn_place30.place_forget()
    btn_place31.place_forget()
    btn_place32.place_forget()
    btn_place33.place_forget()
    btn_place34.place_forget()
    btn_place35.place_forget()
    btn_place36.place_forget()
    btn_place37.place_forget()
    btn_place38.place_forget()
    btn_place39.place_forget()
    btn_place40.place_forget()
    btn_delete_places1.place_forget()
    btn_back1.destroy() 


def check_place():
    global btn_place1
    global btn_place2
    global btn_place3
    global btn_place4
    global btn_place5
    global btn_place6
    global btn_place7
    global btn_place8
    global btn_place9
    global btn_place10
    global btn_place11
    global btn_place12
    global btn_place13
    global btn_place14
    global btn_place15
    global btn_place16
    global btn_place17
    global btn_place18
    global btn_place19
    global btn_place20
    global btn_delete_places
    global btn_back

    btn_place21.place_forget()
    btn_place22.place_forget()
    btn_place23.place_forget()
    btn_place24.place_forget()
    btn_place25.place_forget()
    btn_place26.place_forget()
    btn_place27.place_forget()
    btn_place28.place_forget()
    btn_place29.place_forget()
    btn_place30.place_forget()
    btn_place31.place_forget()
    btn_place32.place_forget()
    btn_place33.place_forget()
    btn_place34.place_forget()
    btn_place35.place_forget()
    btn_place36.place_forget()
    btn_place37.place_forget()
    btn_place38.place_forget()
    btn_place39.place_forget()
    btn_place40.place_forget()
    btn_back1.place_forget()
    btn_delete_places1.place_forget()

    btn_back = Button(text="Назад", height=5, width=20, bg='white', command=back)
    btn_back.place(x=1500,y=800)
    btn_delete_places = Button(text="Очистить места", height=5, width=20, bg='white', command=delete_places)
    btn_delete_places.place(x=770,y=800)
    if (sheet['B2'].value) == 0:
        btn_place1 = Button(text="Место 1.1", height=5, width=20, bg='red', command=choice_place)
        btn_place1.place(x=770,y=400)
    elif (sheet['B2'].value) == 1:
        btn_place2 = Button(text="Место 1.1", height=5, width=20, bg='green')
        btn_place2.place(x=770,y=400)
    if (sheet['C2'].value) == 0:
        btn_place3 = Button(text="Место 1.2", height=5, width=20, bg='red', command=choice_place1)
        btn_place3.place(x=970,y=400)
    elif (sheet['C2'].value) == 1:
        btn_place4 = Button(text="Место 1.2", height=5, width=20, bg='green')
        btn_place4.place(x=970,y=400)
    if (sheet['D2'].value) == 0:
        btn_place5 = Button(text="Место 1.3", height=5, width=20, bg='red', command=choice_place2)
        btn_place5.place(x=1160,y=400)
    elif (sheet['D2'].value) == 1:
        btn_place6 = Button(text="Место 1.3", height=5, width=20, bg='green')
        btn_place6.place(x=1160,y=400)
    if (sheet['E2'].value) == 0:
        btn_place7 = Button(text="Место 1.4", height=5, width=20, bg='red', command=choice_place3)
        btn_place7.place(x=1340,y=400)
    elif (sheet['E2'].value) == 1:
        btn_place8 = Button(text="Место 1.4", height=5, width=20, bg='green')
        btn_place8.place(x=1340,y=400)
    if (sheet['F2'].value) == 0:
        btn_place9 = Button(text="Место 1.5", height=5, width=20, bg='red', command=choice_place4)
        btn_place9.place(x=1530,y=400)
    elif (sheet['F2'].value) == 1:
        btn_place10 = Button(text="Место 1.5", height=5, width=20, bg='green')
        btn_place10.place(x=1530,y=400)
    if (sheet['B3'].value) == 0:
        btn_place11 = Button(text="Место 2.1", height=5, width=20, bg='red', command=choice_place5)
        btn_place11.place(x=770,y=500)
    elif (sheet['B3'].value) == 1:
        btn_place12 = Button(text="Место 2.1", height=5, width=20, bg='green')
        btn_place12.place(x=770,y=500)
    if (sheet['C3'].value) == 0:
        btn_place13 = Button(text="Место 2.2", height=5, width=20, bg='red', command=choice_place6)
        btn_place13.place(x=970,y=500)
    elif (sheet['C3'].value) == 1:
        btn_place14 = Button(text="Место 2.2", height=5, width=20, bg='green')
        btn_place14.place(x=970,y=500)
    if (sheet['D3'].value) == 0:
        btn_place15 = Button(text="Место 2.3", height=5, width=20, bg='red', command=choice_place7)
        btn_place15.place(x=1160,y=500)
    elif (sheet['D3'].value) == 1:
        btn_place16 = Button(text="Место 2.3", height=5, width=20, bg='green')
        btn_place16.place(x=1160,y=500)
    if (sheet['E3'].value) == 0:
        btn_place17 = Button(text="Место 2.4", height=5, width=20, bg='red', command=choice_place8)
        btn_place17.place(x=1340,y=500)
    elif (sheet['E3'].value) == 1:
        btn_place18 = Button(text="Место 2.4", height=5, width=20, bg='green')
        btn_place18.place(x=1340,y=500)
    if (sheet['F3'].value) == 0:
        btn_place19 = Button(text="Место 2.5", height=5, width=20, bg='red', command=choice_place9)
        btn_place19.place(x=1530,y=500)
    elif (sheet['F3'].value) == 1:
        btn_place20 = Button(text="Место 2.5", height=5, width=20, bg='green')
        btn_place20.place(x=1530,y=500) 

def check_place1():
    global btn_place21
    global btn_place22
    global btn_place23
    global btn_place24
    global btn_place25
    global btn_place26
    global btn_place27
    global btn_place28
    global btn_place29
    global btn_place30
    global btn_place31
    global btn_place32
    global btn_place33
    global btn_place34
    global btn_place35
    global btn_place36
    global btn_place37
    global btn_place38
    global btn_place39
    global btn_place40
    global btn_delete_places1
    global btn_back1
    btn_place1.place_forget()
    btn_place2.place_forget()
    btn_place3.place_forget()
    btn_place4.place_forget()
    btn_place5.place_forget()
    btn_place6.place_forget()
    btn_place7.place_forget()
    btn_place8.place_forget()
    btn_place9.place_forget()
    btn_place10.place_forget()
    btn_place11.place_forget()
    btn_place12.place_forget()
    btn_place13.place_forget()
    btn_place14.place_forget()
    btn_place15.place_forget()
    btn_place16.place_forget()
    btn_place17.place_forget()
    btn_place18.place_forget()
    btn_place19.place_forget()
    btn_place20.place_forget()
    btn_back.place_forget()
    btn_delete_places.place_forget()


    btn_back1 = Button(text="Назад", height=5, width=20, bg='white', command=back1)
    btn_back1.place(x=1500, y=800)
    btn_delete_places1 = Button(text="Очистить места", height=5, width=20, bg='white', command=delete_places1)
    btn_delete_places1.place(x=770,y=800)
    if (sheet['B8'].value) == 0:
        btn_place21 = Button(text="Место 1.1", height=5, width=20, bg='red', command=choice_place10)
        btn_place21.place(x=770,y=400)
    elif (sheet['B8'].value) == 1:
        btn_place22 = Button(text="Место 1.1", height=5, width=20, bg='green')
        btn_place22.place(x=770,y=400)
    if (sheet['C8'].value) == 0:
        btn_place23 = Button(text="Место 1.2", height=5, width=20, bg='red', command=choice_place11)
        btn_place23.place(x=970,y=400)
    elif (sheet['C8'].value) == 1:
        btn_place24 = Button(text="Место 1.2", height=5, width=20, bg='green')
        btn_place24.place(x=970,y=400)
    if (sheet['D8'].value) == 0:
        btn_place25 = Button(text="Место 1.3", height=5, width=20, bg='red', command=choice_place12)
        btn_place25.place(x=1160,y=400)
    elif (sheet['D8'].value) == 1:
        btn_place26 = Button(text="Место 1.3", height=5, width=20, bg='green')
        btn_place26.place(x=1160,y=400)
    if (sheet['E8'].value) == 0:
        btn_place27 = Button(text="Место 1.4", height=5, width=20, bg='red', command=choice_place13)
        btn_place27.place(x=1340,y=400)
    elif (sheet['E8'].value) == 1:
        btn_place28 = Button(text="Место 1.4", height=5, width=20, bg='green')
        btn_place28.place(x=1340,y=400)
    if (sheet['F8'].value) == 0:
        btn_place29 = Button(text="Место 1.5", height=5, width=20, bg='red', command=choice_place14)
        btn_place29.place(x=1530,y=400)
    elif (sheet['F8'].value) == 1:
        btn_place30 = Button(text="Место 1.5", height=5, width=20, bg='green')
        btn_place30.place(x=1530,y=400)
    if (sheet['B9'].value) == 0:
        btn_place31 = Button(text="Место 2.1", height=5, width=20, bg='red', command=choice_place15)
        btn_place31.place(x=770,y=500)
    elif (sheet['B9'].value) == 1:
        btn_place32 = Button(text="Место 2.1", height=5, width=20, bg='green')
        btn_place32.place(x=770,y=500)
    if (sheet['C9'].value) == 0:
        btn_place33 = Button(text="Место 2.2", height=5, width=20, bg='red', command=choice_place16)
        btn_place33.place(x=970,y=500)
    elif (sheet['C9'].value) == 1:
        btn_place34 = Button(text="Место 2.2", height=5, width=20, bg='green')
        btn_place34.place(x=970,y=500)
    if (sheet['D9'].value) == 0:
        btn_place35 = Button(text="Место 2.3", height=5, width=20, bg='red', command=choice_place17)
        btn_place35.place(x=1160,y=500)
    elif (sheet['D9'].value) == 1:
        btn_place36 = Button(text="Место 2.3", height=5, width=20, bg='green')
        btn_place36.place(x=1160,y=500)
    if (sheet['E9'].value) == 0:
        btn_place37 = Button(text="Место 2.4", height=5, width=20, bg='red', command=choice_place18)
        btn_place37.place(x=1340,y=500)
    elif (sheet['E9'].value) == 1:
        btn_place38 = Button(text="Место 2.4", height=5, width=20, bg='green')
        btn_place38.place(x=1340,y=500)
    if (sheet['F9'].value) == 0:
        btn_place39 = Button(text="Место 2.5", height=5, width=20, bg='red', command=choice_place19)
        btn_place39.place(x=1530,y=500)
    elif (sheet['F9'].value) == 1:
        btn_place40 = Button(text="Место 2.5", height=5, width=20, bg='green')
        btn_place40.place(x=1530,y=500) 


def onClick1():
    canvas.create_line(58,118,270,118, fill="red", width=5, tag="obvodka")
    canvas.create_line(58,118,58,396, fill="red", width=5, tag="obvodka")
    canvas.create_line(58,396,270,396, fill="red", width=5, tag="obvodka")
    canvas.create_line(268,396,268,118, fill="red", width=5, tag="obvodka")
    kinozal_rdbtn1.place(x=750, y=50)
    kinozal_rdbtn2.place(x=1150, y=50)
    kinozal_rdbtn3.place(x=1600, y=50)

def onClick2():
    canvas.create_line(358,118,570,118, fill="red", width=5, tag="obvodka")
    canvas.create_line(358,118,358,396, fill="red", width=5, tag="obvodka")
    canvas.create_line(358,396,570,396, fill="red", width=5, tag="obvodka")
    canvas.create_line(570,396,570,118, fill="red", width=5, tag="obvodka")
    

def choice_place():
    global btn_place2
    sheet['B2'] = None
    sheet['B2'] = 1
    db.save('database.xlsx')
    btn_place2 = Button(text="Место 1.1", height=5, width=20, bg='green')
    btn_place2.place(x=770,y=400)

def choice_place1():
    global btn_place4
    sheet['C2'] = None
    sheet['C2'] = 1
    db.save('database.xlsx')
    btn_place4 = Button(text="Место 1.2", height=5, width=20, bg='green')
    btn_place4.place(x=970,y=400)

def choice_place2():
    global btn_place6
    sheet['D2'] = None
    sheet['D2'] = 1
    db.save('database.xlsx')
    btn_place6 = Button(text="Место 1.3", height=5, width=20, bg='green')
    btn_place6.place(x=1160,y=400)

def choice_place3():
    global btn_place8
    sheet['E2'] = None
    sheet['E2'] = 1
    db.save('database.xlsx')
    btn_place8 = Button(text="Место 1.4", height=5, width=20, bg='green')
    btn_place8.place(x=1340,y=400)

def choice_place4():
    global btn_place10
    sheet['F2'] = None
    sheet['F2'] = 1
    db.save('database.xlsx')
    btn_place10 = Button(text="Место 1.5", height=5, width=20, bg='green')
    btn_place10.place(x=1530,y=400)

def choice_place5():
    global btn_place12
    sheet['B3'] = None
    sheet['B3'] = 1
    db.save('database.xlsx')
    btn_place12 = Button(text="Место 2.1", height=5, width=20, bg='green')
    btn_place12.place(x=770,y=500)

def choice_place6():
    global btn_place14
    sheet['C3'] = None
    sheet['C3'] = 1
    db.save('database.xlsx')
    btn_place14 = Button(text="Место 2.2", height=5, width=20, bg='green')
    btn_place14.place(x=970,y=500)

def choice_place7():
    global btn_place16
    sheet['D3'] = None
    sheet['D3'] = 1
    db.save('database.xlsx')
    btn_place16 = Button(text="Место 2.3", height=5, width=20, bg='green')
    btn_place16.place(x=1160,y=500)    

def choice_place8():
    global btn_place18
    sheet['E3'] = None
    sheet['E3'] = 1
    db.save('database.xlsx')
    btn_place18 = Button(text="Место 2.4", height=5, width=20, bg='green')
    btn_place18.place(x=1340,y=500)  

def choice_place9():
    global btn_place20
    sheet['F3'] = None
    sheet['F3'] = 1
    db.save('database.xlsx')
    btn_place20 = Button(text="Место 2.5", height=5, width=20, bg='green')
    btn_place20.place(x=1530,y=500)                              

def delete_places():
    global btn_place1
    global btn_place3
    global btn_place5
    global btn_place7
    global btn_place9
    global btn_place11
    global btn_place13
    global btn_place15
    global btn_place17
    global btn_place19
    sheet['B2'] = None
    sheet['C2'] = None
    sheet['D2'] = None
    sheet['E2'] = None
    sheet['F2'] = None
    sheet['B3'] = None
    sheet['C3'] = None
    sheet['D3'] = None
    sheet['E3'] = None
    sheet['F3'] = None
    sheet['B2'] = 0
    sheet['C2'] = 0
    sheet['D2'] = 0
    sheet['E2'] = 0
    sheet['F2'] = 0
    sheet['B3'] = 0
    sheet['C3'] = 0
    sheet['D3'] = 0
    sheet['E3'] = 0
    sheet['F3'] = 0
    db.save('database.xlsx')
    btn_place1 = Button(text="Место 1.1", height=5, width=20, bg='red', command=choice_place)
    btn_place1.place(x=770,y=400)
    btn_place3 = Button(text="Место 1.2", height=5, width=20, bg='red', command=choice_place1)
    btn_place3.place(x=970,y=400)
    btn_place5 = Button(text="Место 1.3", height=5, width=20, bg='red', command=choice_place2)
    btn_place5.place(x=1160,y=400)
    btn_place7 = Button(text="Место 1.4", height=5, width=20, bg='red', command=choice_place3)
    btn_place7.place(x=1340,y=400)
    btn_place9 = Button(text="Место 1.5", height=5, width=20, bg='red', command=choice_place4)
    btn_place9.place(x=1530,y=400)
    btn_place11 = Button(text="Место 2.1", height=5, width=20, bg='red', command=choice_place5)
    btn_place11.place(x=770,y=500)
    btn_place13 = Button(text="Место 2.2", height=5, width=20, bg='red', command=choice_place6)
    btn_place13.place(x=970,y=500)
    btn_place15 = Button(text="Место 2.3", height=5, width=20, bg='red', command=choice_place7)
    btn_place15.place(x=1160,y=500)
    btn_place17 = Button(text="Место 2.4", height=5, width=20, bg='red', command=choice_place8)
    btn_place17.place(x=1340,y=500)
    btn_place19 = Button(text="Место 2.5", height=5, width=20, bg='red', command=choice_place9)
    btn_place19.place(x=1530,y=500)

def choice_place10():
    global btn_place22
    sheet['B8'] = None
    sheet['B8'] = 1
    db.save('database.xlsx')
    btn_place22 = Button(text="Место 1.1", height=5, width=20, bg='green')
    btn_place22.place(x=770,y=400)

def choice_place11():
    global btn_place24
    sheet['C8'] = None
    sheet['C8'] = 1
    db.save('database.xlsx')
    btn_place24 = Button(text="Место 1.2", height=5, width=20, bg='green')
    btn_place24.place(x=970,y=400)

def choice_place12():
    global btn_place26
    sheet['D8'] = None
    sheet['D8'] = 1
    db.save('database.xlsx')
    btn_place26 = Button(text="Место 1.3", height=5, width=20, bg='green')
    btn_place26.place(x=1160,y=400)

def choice_place13():
    global btn_place28
    sheet['E8'] = None
    sheet['E8'] = 1
    db.save('database.xlsx')
    btn_place28 = Button(text="Место 1.4", height=5, width=20, bg='green')
    btn_place28.place(x=1340,y=400)

def choice_place14():
    global btn_place30
    sheet['F8'] = None
    sheet['F8'] = 1
    db.save('database.xlsx')
    btn_place30 = Button(text="Место 1.5", height=5, width=20, bg='green')
    btn_place30.place(x=1530,y=400)

def choice_place15():
    global btn_place32
    sheet['B9'] = None
    sheet['B9'] = 1
    db.save('database.xlsx')
    btn_place32 = Button(text="Место 2.1", height=5, width=20, bg='green')
    btn_place32.place(x=770,y=500)

def choice_place16():
    global btn_place34
    sheet['C9'] = None
    sheet['C9'] = 1
    db.save('database.xlsx')
    btn_place34 = Button(text="Место 2.2", height=5, width=20, bg='green')
    btn_place34.place(x=970,y=500)

def choice_place17():
    global btn_place36
    sheet['D9'] = None
    sheet['D9'] = 1
    db.save('database.xlsx')
    btn_place36 = Button(text="Место 2.3", height=5, width=20, bg='green')
    btn_place36.place(x=1160,y=500)    

def choice_place18():
    global btn_place38
    sheet['E9'] = None
    sheet['E9'] = 1
    db.save('database.xlsx')
    btn_place38 = Button(text="Место 2.4", height=5, width=20, bg='green')
    btn_place38.place(x=1340,y=500)  

def choice_place19():
    global btn_place40
    sheet['F9'] = None
    sheet['F9'] = 1
    db.save('database.xlsx')
    btn_place40 = Button(text="Место 2.5", height=5, width=20, bg='green')
    btn_place40.place(x=1530,y=500)                              

def delete_places1():
    global btn_place21
    global btn_place23
    global btn_place25
    global btn_place27
    global btn_place29
    global btn_place21
    global btn_place23
    global btn_place25
    global btn_place27
    global btn_place29


    sheet['B8'] = None
    sheet['C8'] = None
    sheet['D8'] = None
    sheet['E8'] = None
    sheet['F8'] = None
    sheet['B9'] = None
    sheet['C9'] = None
    sheet['D9'] = None
    sheet['E9'] = None
    sheet['F9'] = None
    sheet['B8'] = 0
    sheet['C8'] = 0
    sheet['D8'] = 0
    sheet['E8'] = 0
    sheet['F8'] = 0
    sheet['B9'] = 0
    sheet['C9'] = 0
    sheet['D9'] = 0
    sheet['E9'] = 0
    sheet['F9'] = 0
    db.save('database.xlsx')
    btn_place21 = Button(text="Место 1.1", height=5, width=20, bg='red', command=choice_place)
    btn_place21.place(x=770,y=400)
    btn_place23 = Button(text="Место 1.2", height=5, width=20, bg='red', command=choice_place1)
    btn_place23.place(x=970,y=400)
    btn_place25 = Button(text="Место 1.3", height=5, width=20, bg='red', command=choice_place2)
    btn_place25.place(x=1160,y=400)
    btn_place27 = Button(text="Место 1.4", height=5, width=20, bg='red', command=choice_place3)
    btn_place27.place(x=1340,y=400)
    btn_place29 = Button(text="Место 1.5", height=5, width=20, bg='red', command=choice_place4)
    btn_place29.place(x=1530,y=400)
    btn_place31 = Button(text="Место 2.1", height=5, width=20, bg='red', command=choice_place5)
    btn_place31.place(x=770,y=500)
    btn_place33 = Button(text="Место 2.2", height=5, width=20, bg='red', command=choice_place6)
    btn_place33.place(x=970,y=500)
    btn_place35 = Button(text="Место 2.3", height=5, width=20, bg='red', command=choice_place7)
    btn_place35.place(x=1160,y=500)
    btn_place37 = Button(text="Место 2.4", height=5, width=20, bg='red', command=choice_place8)
    btn_place37.place(x=1340,y=500)
    btn_place39 = Button(text="Место 2.5", height=5, width=20, bg='red', command=choice_place9)
    btn_place39.place(x=1530,y=500)



btn_back = Button(text="Назад", height=5, width=20, bg='white', command=back)
btn_back1 = Button(text="Назад", height=5, width=20, bg='white', command=back1)
btn_delete_places = Button(text="Очистить места", height=5, width=20, bg='white', command=delete_places)
btn_delete_places1 = Button(text="Очистить места", height=5, width=20, bg='white', command=delete_places1)
btn_place1 = Button(text="Место 1.1", height=5, width=20, bg='red', command=choice_place)
btn_place2 = Button(text="Место 1.1", height=5, width=20, bg='green')
btn_place3 = Button(text="Место 1.2", height=5, width=20, bg='red', command=choice_place1)
btn_place4 = Button(text="Место 1.2", height=5, width=20, bg='green')
btn_place5 = Button(text="Место 1.3", height=5, width=20, bg='red', command=choice_place2)
btn_place6 = Button(text="Место 1.3", height=5, width=20, bg='green')
btn_place7 = Button(text="Место 1.4", height=5, width=20, bg='red', command=choice_place3)
btn_place8 = Button(text="Место 1.4", height=5, width=20, bg='green')
btn_place9 = Button(text="Место 1.5", height=5, width=20, bg='red', command=choice_place4)
btn_place10 = Button(text="Место 1.5", height=5, width=20, bg='green')
btn_place11 = Button(text="Место 2.1", height=5, width=20, bg='red', command=choice_place5)
btn_place12 = Button(text="Место 2.1", height=5, width=20, bg='green')
btn_place13 = Button(text="Место 2.2", height=5, width=20, bg='red', command=choice_place6)
btn_place14 = Button(text="Место 2.2", height=5, width=20, bg='green')
btn_place15 = Button(text="Место 2.3", height=5, width=20, bg='red', command=choice_place7)
btn_place16 = Button(text="Место 2.3", height=5, width=20, bg='green')
btn_place17 = Button(text="Место 2.4", height=5, width=20, bg='red', command=choice_place8)
btn_place18 = Button(text="Место 2.4", height=5, width=20, bg='green')
btn_place19 = Button(text="Место 2.5", height=5, width=20, bg='red', command=choice_place9)
btn_place20 = Button(text="Место 2.5", height=5, width=20, bg='green')
btn_place21 = Button(text="Место 1.1", height=5, width=20, bg='red', command=choice_place10)
btn_place22 = Button(text="Место 1.1", height=5, width=20, bg='green')
btn_place23 = Button(text="Место 1.2", height=5, width=20, bg='red', command=choice_place11)
btn_place24 = Button(text="Место 1.2", height=5, width=20, bg='green')
btn_place25 = Button(text="Место 1.3", height=5, width=20, bg='red', command=choice_place12)
btn_place26 = Button(text="Место 1.3", height=5, width=20, bg='green')
btn_place27 = Button(text="Место 1.4", height=5, width=20, bg='red', command=choice_place13)
btn_place28 = Button(text="Место 1.4", height=5, width=20, bg='green')
btn_place29 = Button(text="Место 1.5", height=5, width=20, bg='red', command=choice_place14)
btn_place30 = Button(text="Место 1.5", height=5, width=20, bg='green')
btn_place31 = Button(text="Место 2.1", height=5, width=20, bg='red', command=choice_place15)
btn_place32 = Button(text="Место 2.1", height=5, width=20, bg='green')
btn_place33 = Button(text="Место 2.2", height=5, width=20, bg='red', command=choice_place16)
btn_place34 = Button(text="Место 2.2", height=5, width=20, bg='green')
btn_place35 = Button(text="Место 2.3", height=5, width=20, bg='red', command=choice_place17)
btn_place36 = Button(text="Место 2.3", height=5, width=20, bg='green')
btn_place37 = Button(text="Место 2.4", height=5, width=20, bg='red', command=choice_place18)
btn_place38 = Button(text="Место 2.4", height=5, width=20, bg='green')
btn_place39 = Button(text="Место 2.5", height=5, width=20, bg='red', command=choice_place19)
btn_place40 = Button(text="Место 2.5", height=5, width=20, bg='green')



canvas = Canvas(boss_menu, width = 19200, height=1080, bg="white") 
canvas.pack()
canvas.create_line(700,0,700,1080, fill="black", tag="lines")
canvas.create_line(700,150,1920,150, fill="black", tag="lines")
canvas.create_line(700,150,1920,150, fill="black", tag="lines")
canvas.create_line(700,300,1920,300, fill="black", tag="lines")
canvas.create_line(750, 350, 1700, 350, fill="black", tag="lines")
canvas.create_line(750, 350, 750, 1000, fill="black", tag="lines")
canvas.create_line(750, 1000, 1700, 1000, fill="black", tag="lines")
canvas.create_line(1700, 1000, 1700, 350, fill="black", tag="lines")
b1 = Button(window, fg="white", bg = "white", command=onClick1)
b2 = Button(window, fg="white", bg = "white", command=onClick2)
b3 = Button(window, fg="white", bg = "white")
b4 = Button(window, fg="white", bg = "white")
b5 = Button(window, fg="white", bg = "white")
b6 = Button(window, fg="white", bg = "white")
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
seansi = Label(window, text="Сеансы на сегодня", bg="white", font=("Arial", 30))
seansi.place(x=140, y=50)
fon = IntVar()
fon.set(1)


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

        spravka.add_command(label="Просмотреть справку", command=help1)
        spravka.add_separator()
        spravka.add_command(label="О программе", command=about_programm)

        menu.add_cascade(label="Данные", menu=file_menu)
        menu.add_cascade(label="Вид", menu=view)
        menu.add_cascade(label="Справка", menu=spravka)
        menu.add_command(label="Выход", command=window.destroy)
        window.config(menu=menu)





def change_view():
    if fon.get() == 1:
        canvas['bg'] = "white"
        canvas.itemconfig('obvodka', fill="red")
        canvas.itemconfig('lines',fill="black")
        s.configure('Wild.TRadiobutton', background=white_color, foreground="black")
    elif fon.get() == 2:
        canvas['bg'] = "#333333" 
        canvas.itemconfig('obvodka', fill="#33FF33")
        canvas.itemconfig('lines',fill="white")
        s1.configure('Wild.TRadiobutton', background=black_color, foreground="white")
        seansi = Label(window, text="Сеансы на сегодня", bg="#333333", foreground="white", font=("Arial", 30))
        seansi.place(x=140, y=50)



def check_answer():
    if var.get() == 1:
        btn_time3.place_forget()
        btn_time4.place_forget()
        btn_time5.place_forget()
        btn_time6.place_forget()
        btn_time1.place(x=800, y=185)
        btn_time2.place(x=1400, y=185)
    elif var.get() == 2:
        btn_time1.place_forget()
        btn_time2.place_forget()
        btn_time5.place_forget()
        btn_time6.place_forget()
        btn_time3.place(x=800, y=185)
        btn_time4.place(x=1400, y=185)
    elif var.get() == 3:
        btn_time1.place_forget()
        btn_time2.place_forget()
        btn_time3.place_forget()
        btn_time4.place_forget()
        btn_time5.place(x=800, y=185)
        btn_time6.place(x=1400, y=185)

     
btn_time1 = Button(text=(sheet['A2'].value), font=("Arial", 30), command=check_place)
btn_time2 = Button(text=(sheet['A8'].value), font=("Arial", 30), command=check_place1)
btn_time3 = Button(text=(sheet['H2'].value), font=("Arial", 30), command=check_place)
btn_time4 = Button(text=(sheet['H8'].value), font=("Arial", 30))
btn_time5 = Button(text=(sheet['O2'].value), font=("Arial", 30))
btn_time6 = Button(text=(sheet['O8'].value), font=("Arial", 30))

kinozal_rdbtn1 = Radiobutton(text="Кинозал 1", variable=var, value=1, style = 'Wild.TRadiobutton', command=check_answer)
kinozal_rdbtn2 = Radiobutton(text="Кинозал 2", variable=var, value=2, style = 'Wild.TRadiobutton', command=check_answer)
kinozal_rdbtn3 = Radiobutton(text="Кинозал 3", variable=var, value=3, style = 'Wild.TRadiobutton', command=check_answer)

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


def help1():
    help12 = tk.Toplevel(window)
    help12.title("Справка")
    help12.geometry("520x350")
    help12.resizable(width=False, height=False)
    help12['bg'] = "white"
    help12 = Canvas(help12, width = 520, height=350, bg='white') 
    help12.pack()
    help12.create_text(250,80,fill="black", font="Arial 12", text="В главном окне вас встречают постеры фильмов")
    help12.create_text(250,100,fill="black", font="Arial 12", text="По которым необходимо кликнуть")
    help12.create_text(250,120,fill="black", font="Arial 12", text="для перехода в окно бронирования мест.")
    help12.create_text(250,140,fill="black", font="Arial 12", text="Необходимо выбрать возможные сеансы и")
    help12.create_text(251,160,fill="black", font="Arial 12", text="выбрать места и нажать кнопку")
    help12.create_text(250,180,fill="black", font="Arial 12", text="Забронировать места")
    help12.create_text(250,200,fill="black", font="Arial 12", text="Так же сверху в главном меню ")
    help12.create_text(250,220,fill="black", font="Arial 12", text="можно изменить вид отображения")
    help12.create_text(250,240,fill="black", font="Arial 12", text="В 'Файл' можно узнать дополнительные")
    help12.create_text(250,260,fill="black", font="Arial 12", text="данные о билетах, местах и т.д.")
    help12.create_text(250,280,fill="black", font="Arial 12", text="В 'Справка' можно открыть вкладку 'о программе'")
    help12.create_text(250,300,fill="black", font="Arial 12", text="узнать информацию о разработке приложения")
    help12.mainloop()


if __name__ == "__main__":
    app = Panel()
    window.mainloop()
    

