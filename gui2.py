from tkinter import *
from random import *
 
def background():
    x = randrange(255)
    y = randrange(255)
    z = randrange(255)
    rgb_color = [x,y,z]
    mycolor = '#%02x%02x%02x' % (x, y, z)
    app.configure(bg=mycolor)
    label1.configure(text=rgb_color)
 
app = Tk()
app.geometry("500x400+5+5")
app.resizable(0,0)
app.title("Color Code")
button1 = Button(app, text="Change", command=background)
button1.pack()
label1 = Label(app, text="")
label1.pack()
app.mainloop()