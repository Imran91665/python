from tkinter import *
from tkinter import font
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("Digital Clock")
def time():
    string=strftime('%H:%M:%S %p')
    Label.config(text=string)
    Label.after(1000,time)
Label=Label(root,font="DS-DIGII 100",background="black",foreground="olive")
Label.pack(anchor='center')
time()
mainloop()