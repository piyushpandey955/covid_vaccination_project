from tkinter import*
from PIL import ImageTk , Image

root=Tk()
canvas=Canvas(root,width=300,height=160)
image=ImageTk.PhotoImage(Image.open("G:\\project jarves\\school project\\pic.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

root.mainloop()