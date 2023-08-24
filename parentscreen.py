from distutils import command
from tkinter import *
from tkinter import ttk as x
import tkinter.messagebox as m
import os
from PIL import Image, ImageTk

m1= Tk()
m1.title('HOME SCREEN')
m1.geometry('600x550')
m1['background']='black'
m1.resizable(False,False)


def openotpverification():
    os.system('python otpgui.py')

def covidtracker():
    os.system('python covid_tracker1.py')

def vaccineslotcheck():
    os.system('python vaccineslotgui1.py')

canvas=Canvas(m1,width=600,height=550)
image=ImageTk.PhotoImage(Image.open("E:\\pp\\project jarves\\python\\dpsg covid project\\school project\\files\\pic.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()


t=Label(m1,text='WELCOME P.S.M COVID APPLICATION !',bg='black',fg='#00e3ff',font=('Bell MT',16))
t.place(x=100,y=60)
b1=Button(m1,text='VACCINE REGISTRATION',bg='black',fg='#00e3ff',font=('Bell MT',16),command=openotpverification)
b1.place(x=150,y=110)
b2=Button(m1,text="COVID CASES INFORMATION",bg="black",fg='#00e3ff',font=('Bell MT',16),command=covidtracker)
b2.place(x=150,y=170)
b3=Button(m1,text="COVID VACCINE AVALABLITY CENTERS",bg="black",fg='#00e3ff',font=("Bell MT",16), command=vaccineslotcheck)
b3.place(x=150,y=230)




mainloop()