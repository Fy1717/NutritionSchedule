# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.title( "Beslenme ve Diyet Programı" )

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 320
window_height = 250

window_position_x = 0
window_position_y = 0
root.geometry("320x250")

frame = tk.Frame(root, bg='cyan')
frame.pack(side="bottom", fill='both', expand='no')

lengthLabel = Label(root,width=20,height=3,text="BOYUNUZ   :" , font="Times 10 bold")
lengthLabel.place(x=5 ,y=26)

weightLabel = Label(root,width=20,height=3,text="KİLONUZ    :" , font="Times 10 bold")
weightLabel.place(x=5,y=66)

lengthLabel = Label(root,width=40,height=3,text="www.frknyldz.com" , font="Times 10 bold")
lengthLabel.place(x=5 ,y=206)


length_edit = Entry(root,width=15)
length_edit.place(x=150,y=40)
length_edit.config(font="bold")
length_edit.insert(END,"")

weight_edit = Entry(root,width=15)
weight_edit.place(x=150,y=80)
weight_edit.config(font="bold")
weight_edit.insert(END,"")


# Kullanıcı Kontrol Fonksiyonu
def Calculater():
    Boy = float(length_edit.get())
    Kilo = float(weight_edit.get())
    Index = Kilo/((Boy/100)*2)

    if (Index <= 18.0):
        tk.messagebox.showinfo("Zayıf !! \r\n", "MENÜ  : \n --------- \n*Bonfile\n*Bol Ekmek\n*Kola\n*Baklava")

    elif (Index <= 25.0):
        tk.messagebox.showinfo("Normal !! \r\n", "MENÜ  : \n --------- \n*Bonfile\n*Bol Ekmek\n*Kola\n*Baklava")


    elif (Index <= 30.0):
        tk.messagebox.showinfo("Kilolu !! \r\n", "MENÜ  : \n --------- \n*Bonfile\n*Bol Ekmek\n*Kola\n*Baklava ")

    elif (Index <= 35.0):
        tk.messagebox.showinfo("1.Derece Obez !! \r\n", "MENÜ  : \n --------- \n*Bonfile\n*Bol Ekmek\n*Kola\n*Baklava ")

    elif (Index <= 40.0):
        tk.messagebox.showinfo("2.Derece Obez !! \r\n", "MENÜ  : \n --------- \n*Bonfile\n*Bol Ekmek\n*Kola\n*Baklava")

    elif (Index >= 40.0):
        tk.messagebox.showinfo("3.Derece Obez !! \r\n", "MENÜ  : \n --------- \n*Bonfile\n*Bol Ekmek\n*Kola\n*Baklava")



# Giriş Alanlarını Temizleme Fonksiyonu
def Clear():
    length_edit.delete('1.0',END)
    weight_edit.delete('1.0',END)



# Giriş Butonu
controlButton = Button(root,text="HESAPLA",width=30,command=Calculater)
controlButton.config(font="bold")
controlButton.place(x=10,y=150)



root.mainloop()



