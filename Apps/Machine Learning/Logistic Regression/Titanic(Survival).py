import tkinter as ttk
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Reading Our Model
model=pd.read_pickle('Titanic(Machine_learning).pickle')
col=['Sex_male','Fare','Age']

app=ttk.Tk()
app.title("Titanic Survival Prediction")
app.geometry('300x200')

ttk.Label(app,text="Choose Gender",font=("Arial",10),padx=20,pady=20).grid(row=0,column=0)
#We will be making a dictionary for gender where male :1 female : 0
Gender={'Male':1,'Female':0}
Gender_Var=ttk.Variable(app)
Gender_Var.set(Gender['Male'])
frame=ttk.Frame(app)
frame.grid(row=0,column=1)
for gender,gender_value in Gender.items():
    ttk.Radiobutton(frame,text=gender,variable=Gender_Var,value=gender_value).pack(side=ttk.LEFT)

#Fare
Fare=ttk.DoubleVar(app)
Fare.set(0)
ttk.Label(app,text="Fare",font=("Arial",10)).grid(row=1,column=0)
ttk.Spinbox(app,from_=0,to_=100,textvariable=Fare,width=15).grid(row=1,column=1)



#Age
Age=ttk.IntVar(app)
Age.set(0)
ttk.Label(app,text="Age",font=("Arial",10)).grid(row=2,column=0)
ttk.Spinbox(app,from_=0,to_=100,textvariable=Age,width=15).grid(row=2,column=1)


result=ttk.Variable(app)
ttk.Label(app,textvariable=result,font=("Arial",10)).grid(row=3,column=1)


# Defining our Prediction Model
def predict():
    global model
    sample_data=pd.DataFrame({'Sex_male':[Gender_Var.get()],'Fare':[Fare.get()],'Age':[Age.get()]})
    pred=model.predict(sample_data)
    if pred[0]==1:
        result.set('Might Survive')
    else:
        result.set('Might not Survive')

# Creating button to show 
ttk.Button(app,text="Predict",command=predict,font=("Arial",10)).grid(row=3,column=0)





















app.mainloop()