from pydoc import TextRepr
from pyexpat import model
import tkinter as ttk
from turtle import color
import pandas as pd

model=pd.read_pickle('SurvivalPrediction.pickle')
app=ttk.Tk()
app.geometry('600x600')
app.title('Titanic Survival Prediction')

col=['Sex_male','Fare','Age']

ttk.Label(app,text='Choose Gender', padx=20,pady=20).grid(row=0,column=0)
genders = {'Male': 1, 'Female': 0}
genderVar=ttk.Variable(app)
genderVar.set(genders['Male'])
frame=ttk.Frame(app)
frame.grid(row=0,column=1)
for gender,genderValue in genders.items(): 
    ttk.Radiobutton(frame,text=gender,variable=genderVar,value=genderValue).pack(side=ttk.LEFT)

#Fare
ttk.Label(app,text="Enter Fare",padx=20,pady=20).grid(row=1,column=0)
fareVar=ttk.DoubleVar(app)
ttk.Spinbox(app,from_=0, to=10000,textvariable=fareVar,width=10).grid(row=1,column=1)
# ttk.Entry(app,textvariable=fareVar).grid(row=1,column=1)


#Age
ttk.Label(app,text="Age",padx=20,pady=20).grid(row=2,column=0)
ageVar=ttk.IntVar(app)
ageVar.set(0)
ttk.Spinbox(app,from_=0, to=100,textvariable=ageVar,width=10).grid(row=2,column=1)
# ttk.Entry(app,textvariable=ageVar).agrid(row=2,column=1)
resultvar=ttk.Variable(app)

#Predict Button
def find_survival():
    global model
    query_df=pd.DataFrame({'Sex_male':[genderVar.get()],'Fare':[fareVar.get()],'Age':[ageVar.get()]})
    pred= model.predict(query_df)
    if pred[0]==1:
        resultvar.set('Might Survive!')
    else:
        resultvar.set('Might not Survive!')
    return 










ttk.Button(app,text='check',command=find_survival,padx=20,pady=10).grid(row=3,column=0,columnspan=2)

ttk.Label(app,textvariable=resultvar,font=('Arial',20)).grid(row=4,column=0,columnspan=2)

app.mainloop()