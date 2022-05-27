from functools import partial
from glob import glob
import tkinter as tk



Calculator=tk.Tk()
Calculator.title("Calculator")
#Calculator.geometry("400x200")
global num
num=''


def Calcul(symbole):
    global num
    if symbole=='RESET':
        num=''
    elif type(symbole) == type(1):
        num=num+str(symbole)
    elif type(symbole) == type('+'):
        num=num+str(symbole)
    result=tk.Label(Calculator, text=num)
    result.grid(column=2,row=1)
    return 

def affichage():
    print('num')
    tk.Button(Calculator, text='1', width=3, height=3, command=partial(Calcul,1)).grid(column=1,row=2)
    tk.Button(Calculator, text='2', width=3, height=3, command=partial(Calcul,2)).grid(column=2, row=2)
    tk.Button(Calculator, text='3', width=3, height=3, command=partial(Calcul,3)).grid(column=3, row=2)
    tk.Button(Calculator, text='4', width=3, height=3, command=partial(Calcul,4)).grid(column=1, row=3)
    tk.Button(Calculator, text='5', width=3, height=3, command=partial(Calcul,5)).grid(column=2, row=3)
    tk.Button(Calculator, text='6', width=3, height=3, command=partial(Calcul,6)).grid(column=3, row=3)
    tk.Button(Calculator, text='7', width=3, height=3, command=partial(Calcul,7)).grid(column=1, row=4)
    tk.Button(Calculator, text='8', width=3, height=3, command=partial(Calcul,8)).grid(column=2, row=4)
    tk.Button(Calculator, text='9', width=3, height=3, command=partial(Calcul,9)).grid(column=3, row=4)

    

    result=tk.Label(Calculator, text='')
    result.grid(column=2,row=1)
    Calculator.mainloop()

affichage()