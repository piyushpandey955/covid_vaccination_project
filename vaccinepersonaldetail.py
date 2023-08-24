from tkinter import *
import tkinter.messagebox as m
from PIL import Image, ImageTk


m1=Tk()
m1.title("PERSONAL DETAIL INPUT")
m1.geometry("1285x720")
m1["background"]="black"
m1.resizable(False,False)


namevar=StringVar()
fnamevar=StringVar()
addressvar=StringVar()
phonevar=StringVar()
aadharvar=StringVar()
agevar=StringVar()
gendervar=StringVar()

canvas=Canvas(m1,width=1285,height=720)
image=ImageTk.PhotoImage(Image.open("E:\\pp\\project jarves\\python\\dpsg covid project\\school project\\files\\pic2.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

a=namevar.get()
print(a)

def verifypersonaldetails():
    m.showinfo("myproject","registration succesful")
    '''n=namevar
    if n.isalpha()==True:
        return n
    else:
        print("invalid name")
    
    age=agevar
    if age.isnumeric():
        return age
        if (age<18):
             print("you are not eligible for vaccination")
    else:
        print("invalid age")
    
    phone_num=phonevar
    if (len(phone_num)==10 and phone_num.isnumeric()):
        return phone_num
    else:
        print("invalid no.")'''

t=Label(m1,text='PLEASE PROVIDE YOUR PERSONAL DETAILS !',bg='black',fg='#00e3ff',font=('Bell MT',16))
t.place(x=490,y=8)
l1=Label(m1,text='ENTER NAME',bg='black',fg='#00e3ff',font=('Bell MT',14))
l1.place(x=100,y=95)
l2=Label(m1,text='ENTER FATHER NAME',bg='black',fg='#00e3ff',font=('Bell MT',14))
l2.place(x=350,y=95)
l3=Label(m1,text='ENTER PHONE NUMBER',bg='black',fg='#00e3ff',font=('Bell MT',14))
l3.place(x=700,y=95)
l4=Label(m1,text='ENTER YOUR AGE',bg='black',fg='#00e3ff',font=('Bell MT',14))
l4.place(x=100,y=200)
l5=Label(m1,text='ENTER YOUR GENDER',bg='black',fg='#00e3ff',font=('Bell MT',14))
l5.place(x=400,y=200)
l6=Label(m1,text='ENTER YOUR AADHAR NO.',bg='black',fg='#00e3ff',font=('Bell MT',14))
l6.place(x=700,y=200)
l7=Label(m1,text='ENTER YOUR ADDRESS',bg='black',fg='#00e3ff',font=('Bell MT',14))
l7.place(x=400,y=400)


e1=Entry(m1,textvariable=namevar)
e1.place(x=100,y=135)
e2=Entry(m1,textvariable=fnamevar)
e2.place(x=350,y=135)
e3=Entry(m1,textvariable=phonevar)
e3.place(x=700,y=135)
e4=Entry(m1,textvariable=agevar)
e4.place(x=100,y=240)
e5=Entry(m1,textvariable=gendervar)
e5.place(x=400,y=240)
e6=Entry(m1,textvariable=aadharvar)
e6.place(x=700,y=240)
e7=Entry(m1,textvariable=addressvar)
e7.place(x=400,y=440)




b1=Button(m1,text='SUBMIT DETAILS',bg='black',fg='#00e3ff',font=('Bell MT',16),command=verifypersonaldetails)
b1.place(x=500,y=600)



mainloop()