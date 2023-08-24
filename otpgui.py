from tkinter import *
from tkinter import ttk as x
import random
import smtplib
import tkinter.messagebox as m
import os
from PIL import Image, ImageTk

# window creation and design 
m4= Tk()
m4.title('otp verifiaction')
m4.geometry('600x550')
m4['background']='black'
m4.resizable(False,False)


canvas=Canvas(m4,width=600,height=550)
image=ImageTk.PhotoImage(Image.open("E:\\pp\\project jarves\\python\\dpsg covid project\\school project\\files\\pic3.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()


otpvar=StringVar()
emailvar=StringVar()


'''def sendemail():
    p=emailvar.get()
    print(p) #p=gmail'''

    #otp block 
def sendotp():
    global otp
    global receiver
    # sending otp
    p=emailvar.get()
    print(p) #p=gmail
    otp=random.randint(100000,1000000)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("meenumeenu14282004@gmail.com","owocgnqphdpwuazq")
    msg="hello your otp is"+str(otp)
    receiver=p
    server.sendmail("meenumeenu14282004@gmail.com",receiver,msg)
    server.quit()

    # fetching otp for internal logic
    s=otpvar.get()
    print(s) # s=otp

def submitotp():
    s=otpvar.get()
    if s==str(otp):
        print("verification successful")
        m.showinfo("myproject","verification succesful")
        os.system('python vaccinepersonaldetail.py')

    else:
        print("verification unsuccesful") 
        m.showinfo("myproject","verification unsuccesful")   
        
    #resend otp block
    def resendotp():
        otp=random.randint(100000,1000000)

        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("meenumeenu14282004@gmail.com","owocgnqphdpwuazq")
        msg="hello your otp is"+str(otp)   
        receiver1=receiver    
        server.sendmail("meenumeenu14282004@gmail.com",receiver,msg)
        server.quit()
        s=otpvar.get()
        print(s)
            
            

##buttons and text creation
t=Label(m4,text='Welcome to vaccination registration system !',bg='black',fg='#00e3ff',font=('Bell MT',16))
b1=Button(m4,text='SUBMIT OTP',bg='black',fg='#00e3ff',font=('Bell MT',16),command=submitotp)
b2=Button(m4,text='RESEND OTP',bg='black',fg='#00e3ff',font=('Bell MT',16))#,command= resendotp)
b3=Button(m4,text="SUBMIT EMAIL",bg='black',fg='#00e3ff',font=('Bell MT',16),command=sendotp)
e1=Entry(m4,textvariable=otpvar)
e1.place(x=215,y=250)
e2=Entry(m4,textvariable=emailvar)
e2.place(x=215,y=100)


##buttons and text placing
t.place(x=100,y=60)
b1.place(x=222,y=300)
b2.place(x=208,y=400)
b3.place(x=200,y=150)


mainloop()