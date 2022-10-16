import tkinter as ttk
from turtle import bgcolor
import pandas as pd
import numpy as np

app=ttk.Tk()
app.title('Calculator')
app.geometry('500x500')

ttk.Label(app,text='Calculator',font=("Arial",30)).place(x=170,y=10)
#Creating two Variables
func1=ttk.Variable(app)
func1.set(0)

func2=ttk.Variable(app)
func2.set(0)
#Creating a Variable for Result
result=ttk.Variable(app)

#Creating two Entries:
#Python Tkinter entry is among the most generally used graphical user interface in python to design textboxes in GUIs.
#These are used to create editable text boxes where we can input something at runtime of an app
ttk.Entry(app,textvariable=func1).place(x=120,y=80)
ttk.Entry(app,textvariable=func2).place(x=120,y=140)
ttk.Entry(app,textvariable=result).place(x=120,y=200)


def cal(operator):
    print("Calculated")
    result.set(eval(func1.get()+operator+func2.get()))#This Eval function will read the string as python code then evaluate it
   
ttk.Button(app,text='+',command=lambda:cal("+")).place(x=300,y=80)
ttk.Button(app,text='-',command=lambda:cal("-")).place(x=300,y=120)
ttk.Button(app,text='*',command=lambda:cal("*")).place(x=300,y=160)
ttk.Button(app,text='/',command=lambda:cal("/")).place(x=300,y=200)





app.mainloop()