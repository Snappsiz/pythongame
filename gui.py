from tkinter import *
import time


root=Tk()
txt = StringVar()

def check():
    if txt.get() == "start":
        libl1.configure(text="Game starts")
        btn1.configure(text="Select Option")
        ent1.delete(0, END)
    else:
        libl1.configure(text="type start to start the game")
        
libl1= Label(root, text="Welcome to my test game. Type start to continue!")
libl1.pack()
ent1= Entry(root, textvariable=txt)
ent1.pack()
btn1= Button(root, text="Enter!", command=check)
btn1.pack()



root.mainloop()
