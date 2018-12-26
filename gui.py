from tkinter import *
import time


root=Tk()
txt = StringVar()

def check():
    x=txt.get()
    if x:
        libl1.configure(text="The game continues.") 
    else:
        print("try again!")


libl1= Label(root, text="Welcome to my test game. Type start to continue!")
libl1.pack()
ent1= Entry(root, textvariable=txt)
ent1.pack()
btn1= Button(root, text="Enter!", command=check)
btn1.pack()



root.mainloop()