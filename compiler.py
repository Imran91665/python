
from cProfile import label
import code
from concurrent.futures import process
from distutils.log import error
from importlib.resources import path
from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
from turtle import color

from matplotlib.pyplot import text
compiler= Tk()
compiler.title('PyCom')
file_path= ''
def set_file_path(path):
    global file_path
    file_path=path




def open_file():
    path=askopenfilename(filetypes=[('python files','*.py')])
    with open(path,'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)
        

def save_as():
    if file_path=='':
     path=asksaveasfilename(filetypes=[('python files','*.py')])
    else:
        path=file_path
    with open(path,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)
def run():
    if file_path == '':
        save_promt=Toplevel()
        text=Label(save_promt,text='please save')
        text.pack()
        return

    command=f'python{file_path}'
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output, error=process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)

menu_var=Menu(compiler)
file_menu=Menu(menu_var,tearoff=0)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_as)
file_menu.add_command(label='Save_as',command=save_as)
file_menu.add_command(label='Exit',command=exit)
menu_var.add_cascade(label='File',menu=file_menu)

run_var=Menu(menu_var,tearoff=0)
run_var.add_command(label='Run',command=run)
menu_var.add_cascade(label='Run',menu=run_var)
compiler.config(menu=menu_var)


editor=Text()
editor.pack()
code_output=Text(height=15,background='black',foreground='white')
code_output.pack()
compiler.mainloop()
