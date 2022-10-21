from logging import warning
import tkinter as ttk
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from PIL import ImageTk,Image

app=ttk.Tk()
app.title("Treadmill User")
app.geometry('1000x1000')

df=pd.read_csv('treadmil-users.csv')


ttk.Label(app,text='Graphs on Treadmill Users',font=('Arial',25)).place(x=450,y=10)


graphs=ttk.Variable(app)
#Making up dictionary for different types of buttons showing multiple options for graph
Values={'Pair Plot':"sns.pairplot(data=df)",
        'Joint Plot':"sns.jointplot(data=df , x='{col1}', y='{col2}')",
        'Bar Plot'  : "sns.barplot(data=df , x='{col1}', y='{col2}')",
        'Box Plot'  : "sns.boxplot(data=df , x='{col1}', y='{col2}')"
        }
graphs.set(Values['Pair Plot'])
y=80
#This will make Buttons for our graphs
for key,values in Values.items():
    ttk.Radiobutton(app,text=key,variable=graphs,value=values).place(x=10,y=y)
    y+=20

#Now we will make Option Value
#1
col1=ttk.Variable(app)
values=['Select']+list(df.columns)
col1.set(values[0])

ttk.Label(app,text="1st Column",font=('Arial',10)).place(x=100,y=80)
ttk.OptionMenu(app,col1,*values).place(x=180,y=80)



#2
col2=ttk.Variable(app)
values=['Select']+list(df.columns)
col2.set(values[0])

ttk.Label(app,text="2nd Column",font=('Arial',10)).place(x=100,y=120)
ttk.OptionMenu(app,col2,*values).place(x=180,y=120)



#3
col3=ttk.Variable(app)
values=['Select']+list(df.columns)
col3.set(values[0])

ttk.Label(app,text="3rd Column",font=('Arial',10)).place(x=100,y=160)
ttk.OptionMenu(app,col3,*values).place(x=180,y=160)

#Canavas
#with the help of this we will show the graphs
cnv=ttk.Canvas(app,width=450,height=350)
cnv.place(x=350,y=100)

#Result

result=ttk.Variable(app)
ttk.Label(app,textvariable=result).place(x=240,y=200)

def show():
    global img
    global cnv
    column1=col1.get()
    column2=col2.get()
    column3=col3.get()

    g=graphs.get()
    
    if 'col1' in g:
        if column1 == 'Select':
            result.set('Column 1 must be selected')
            return
    if 'col2' in g:
        if column2 == 'Select':
            result.set('Column 2 must be selected')
            return 
    if 'col3' in g:
        if column3 == 'Select':
            result.set('Column 3 must be selected')
            return
    fig=plt.figure(figsize=(10,5))
    eval(g.format(col1=column1,col2=column2,col3=column3))
    fig,plt.savefig('graph.png')
    img=ImageTk.PhotoImage(Image.open('graph.png').resize((450,350)))
     
    cnv.create_image(0,0,anchor=ttk.NW,image=img)
    result.set("Suceess")

ttk.Button(app,text="Show",command=show).place(x=240,y=240)






app.mainloop()