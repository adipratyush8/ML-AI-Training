#In order to build GUI -(graphical user interface) , we need to import Libraries
'''
1.tkinter
2.pYQt
3.turtle
'''
import tkinter as ttk
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np

app=ttk.Tk()#This is Tk(Tool kit) we will be building an window 
app.title("First APP")#This will give us title for our window 
app.geometry('600x600')#This will set size

msg=ttk.Variable(app)

msg.set("Aaditya")

'''
Python Tkinter label:
1. The label simply means the text on the screen.
2. It could be an instruction or information.
3. Labels are the widely used widget & is a command in all the GUI supporting tools & languages.
'''
#Creating two Labels (printed text)
ttk.Label(app,text="Hello world",font="Arial").place(x=250,y=10)#arguments for Label (app,text).placing
ttk.Label(app,textvariable=msg,font=('Algerian',25)).place(x=50,y=30)#arguments for Label (app,text).placing
#Here we are using text variable as text 

def abc():
    print('Aaditya')#This will get printed in the terminal
    msg.set('I am 18 years old')


#Creating Two buttons
# Python - Tkinter Button. The Button widget is used to add buttons in a Python application. These buttons can display text or images that convey the purpose of the buttons. 
ttk.Button(app,text='What is your age',command=abc).place(x=100,y=100)#Argument for button are (app,text,command).place()
ttk.Button(app,text=' Where are you from',command=lambda:msg.set('I am from Jaipur')).place(x=200,y=100)#Argument for button are (app,text,command).place()







app.mainloop()