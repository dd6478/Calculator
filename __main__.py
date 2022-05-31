#!/usr/bin/env python3

         ############
        ######by######
        #####dd64#####
         ############ 

from functools import partial
import tkinter as tk

Calculator=tk.Tk()
Calculator.title("Calculator")
#Calculator.geometry("400x200")
num=''

def Calcul(symbole):
    global num
    if symbole == 'RESET':
        num=''
    elif symbole == '=':
        Ops=[]
        for l in num:
            if l == '+' or l == 'x' or l == '-' or l == ':':
                Ops.append(l)
        num=num.replace('+',' ')
        num=num.replace('-',' ')
        num=num.replace('x',' ')
        num=num.replace(':',' ')
        Cal=num.split(' ')
        for i in range(len(Cal)):
            Cal[i]=int(Cal[i])
        L=len(Ops)
        for i in range(L):
            j=0
            if 'x' in Ops or ':' in Ops :
                for Ope in Ops:
                    if Ope == 'x':
                        Ops.pop(j)
                        Cal.insert(j,Cal.pop(j)*Cal.pop(j))       
                    elif Ope == ':':
                        Ops.pop(j)
                        Cal.insert(j,Cal.pop(j)/Cal.pop(j))     
                    j+=1
            elif '+' in Ops or '-' in Ops :
                for Ope in Ops:
                    if Ope == '+':
                        Ops.pop(j)
                        Cal.insert(j,Cal.pop(j)+Cal.pop(j))       
                    elif Ope == '-':
                        Ops.pop(j)
                        Cal.insert(j,Cal.pop(j)-Cal.pop(j))
                    j+=1
        num=Cal[0]
    elif type(symbole) == type(1):
        num=num+str(symbole)
    elif type(symbole) == type('+'):
        num=num+str(symbole)
    A.set(num)
    return 
    
def affichage():
    global num
    global A
    print('num')
    tk.Button(Calculator, text='0', width=3, height=3, command=partial(Calcul,0)).grid(column=2, row=5)
    tk.Button(Calculator, text='1', width=3, height=3, command=partial(Calcul,1)).grid(column=1,row=4)
    tk.Button(Calculator, text='2', width=3, height=3, command=partial(Calcul,2)).grid(column=2, row=4)
    tk.Button(Calculator, text='3', width=3, height=3, command=partial(Calcul,3)).grid(column=3, row=4)
    tk.Button(Calculator, text='4', width=3, height=3, command=partial(Calcul,4)).grid(column=1, row=3)
    tk.Button(Calculator, text='5', width=3, height=3, command=partial(Calcul,5)).grid(column=2, row=3)
    tk.Button(Calculator, text='6', width=3, height=3, command=partial(Calcul,6)).grid(column=3, row=3)
    tk.Button(Calculator, text='7', width=3, height=3, command=partial(Calcul,7)).grid(column=1, row=2)
    tk.Button(Calculator, text='8', width=3, height=3, command=partial(Calcul,8)).grid(column=2, row=2)
    tk.Button(Calculator, text='9', width=3, height=3, command=partial(Calcul,9)).grid(column=3, row=2)

    tk.Button(Calculator, text='+', width=3, height=3, command=partial(Calcul,'+')).grid(column=4, row=4)
    tk.Button(Calculator, text='-', width=3, height=3, command=partial(Calcul,'-')).grid(column=4, row=3)
    tk.Button(Calculator, text='x', width=3, height=3, command=partial(Calcul,'x')).grid(column=4, row=2)
    tk.Button(Calculator, text=':', width=3, height=3, command=partial(Calcul,':')).grid(column=4, row=1)
    tk.Button(Calculator, text='=', width=3, height=3, command=partial(Calcul,'=')).grid(column=4, row=5)
    tk.Button(Calculator, text='AC', width=3, height=3, command=partial(Calcul,'RESET')).grid(column=2, row=1)

    A=tk.StringVar()
    result=tk.Label(Calculator, textvariable=A)
    result.grid(column=1, columnspan=3,row=0)

    Calculator.mainloop()

affichage()
