from email.mime import image
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import requests
import datetime
from PIL import Image, ImageTk
import os

'''top=Tk()
top.geometry("600x550")
fn=PhotoImage(file="C://Users//hp//Desktop//12.png")
background_label=Label(top,image=fn)
background_label.place(x=0,y=0,relwidth=1,relheight=1)'''

canvas = tk.Tk()
canvas.geometry("600x550")
canvas.title("COVID Tracker")
canvas.resizable(False, False)
canvas.config(background = '#ADD8E6')
#image=ImageTk.PhotoImage(Image.open("E:\\pp\\project jarves\\school project\\files\\pic4.png"))
#canvas.create_image(0,0,anchor=NW,image=image)
                
def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    total_recovered = str(json_data['recovered'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    active_cases = str(json_data['active'])
    updated_at = json_data['updated']
    d = datetime.datetime.fromtimestamp(updated_at/1e3) #converts variable to proper date and time
    
    label.config(text ="\n"+"WORLD DATA"+"\n"
                 "\n"+"Total Cases :  "+total_cases+
                 "\n"+"Total Deaths :  "+total_deaths+
                 "\n"+"Total Recovered :  "+total_recovered+
                 "\n"+"\n"+"INDIA"+"\n"
                 "\n"+"Today Cases : "+today_cases+
                 "\n"+"Today Deaths :  "+today_deaths+
                 "\n"+"Today Recovered :  "+today_recovered+
                 "\n"+"Active Cases :  "+active_cases)

    label2.config(text = d)



f=("poppins", 15, 'bold')

button = tk.Button(canvas, font = f, text = "Load Data", command = getCovidData)

button.pack(pady = 20)
label = tk.Label(canvas, font = f)
label.pack(pady = 20)

label2=tk.Label(canvas,font = 8)
label2.pack()


getCovidData()
canvas.mainloop()
