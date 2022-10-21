import pandas as pd
import numpy as np
import tkinter as ttk
import warnings
warnings.filterwarnings('ignore')

model=pd.read_pickle('housePrice.pickel')
app=ttk.Tk()
app.title('House Price Predictor')
app.geometry('600x600')

Income=ttk.Variable(app)

ttk.Label(app,text='Income',padx=15,pady=15).grid(row=0,column=0)
ttk.Entry(app,textvariable=Income,width=10).grid(row=0,column=1)

house_age=ttk.Variable(app)

ttk.Label(app,text='House Age',padx=15,pady=15).grid(row=1,column=0)
ttk.Entry(app,textvariable=house_age,width=10).grid(row=1,column=1)

num_rooms=ttk.Variable(app)

ttk.Label(app,text='Number of rooms',padx=15,pady=15).grid(row=2,column=0)
ttk.Entry(app,textvariable=num_rooms,width=10).grid(row=2,column=1)

Population=ttk.Variable(app)

ttk.Label(app,text='Population',padx=15,pady=15).grid(row=3,column=0)
ttk.Entry(app,textvariable=Population,width=10).grid(row=3,column=1)

def prediciton():
    global model
    query_data={
        'avg. area income':[eval(Income.get())],
        'avg. Area of house age':[eval(house_age.get())],
        'avg. area of number of rooms':[eval(num_rooms.get())],
        'avg. area Population':[eval(Population.get())],
    }
    price=model.predict(pd.DataFrame(query_data))
    result.set(round(price[0],2))
ttk.Button(app,text='Pedict',command=prediciton,font=('Arial',20)).grid(row=4,column=0,columnspan=2)

result=ttk.Variable(app)
result.set('0')
ttk.Label(app,textvariable=result,pady=15,font=('Arial',20)).grid(row=5,column=0,columnspan=2)

app.mainloop()