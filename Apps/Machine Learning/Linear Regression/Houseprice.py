import pandas as pd
import numpy as np
import tkinter as ttk
import warnings
warnings.filterwarnings('ignore')
model=pd.read_pickle('housePrice.pickel')
app=ttk.Tk()
app.title('House Price Prediction')
app.geometry('400x400')
app.config(background='Light Blue')

#We will be creating 4 Entries as our variables to predict the price of the house
Income=ttk.Variable(app)

ttk.Label(app,text="Income",font=("Arial",10),padx=10,pady=10).grid(row=0,column=0)
ttk.Entry(app,textvariable=Income,font=("Arial",10),width=10).grid(row=0,column=1)


House_age=ttk.Variable(app)

ttk.Label(app,text="House Age",font=("Arial",10),padx=10,pady=10).grid(row=1,column=0)
ttk.Entry(app,textvariable=House_age,font=("Arial",10),width=10).grid(row=1,column=1)


NumberofRooms=ttk.Variable(app)

ttk.Label(app,text="Number Of Rooms",font=("Arial",10),padx=10,pady=10).grid(row=2,column=0)
ttk.Entry(app,textvariable=NumberofRooms,font=("Arial",10),width=10).grid(row=2,column=1)


Population=ttk.Variable(app)

ttk.Label(app,text="Population",font=("Arial",10),padx=10,pady=10).grid(row=3,column=0)
ttk.Entry(app,textvariable=Population,font=("Arial",10),width=10).grid(row=3,column=1)





#Now we will making a funcion for prediction
def Prediction():
    global model
    sample_data={
    'avg. area income':[eval(Income.get())],
        'avg. Area of house age':[eval(House_age.get())],
        'avg. area of number of rooms':[eval(NumberofRooms.get())],
        'avg. area Population':[eval(Population.get())],
    }
    price=model.predict(pd.DataFrame(sample_data))
    Result.set(round(price[0],2))
ttk.Button(app,text='Predict',command=Prediction,font=("Arial",15)).grid(row=4,column=0)

Result=ttk.Variable(app)
Result.set(0)
ttk.Label(app,text="Result",font=("Arial",15),padx=10,pady=10).grid(row=5,column=0)
ttk.Label(app,textvariable=Result,font=("Arial",15),).grid(row=5,column=1)


#In order to convert this code into a application (.exe )
#write this in command pyinstaller --onefile -w file_Name






app.mainloop()