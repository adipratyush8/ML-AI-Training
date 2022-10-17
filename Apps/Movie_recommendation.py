import pandas as pd
import tkinter as ttk
import numpy as np
import warnings
import os 
warnings.filterwarnings("ignore")
 

app=ttk.Tk()
app.title("Movie Recommendation")
app.geometry('700x700')
os.getcwd()
ttk.Label(app,text='Movie Recommendation',font=('Arial',25)).place(x=150,y=10)


#Reading 
col=['user-id','movie-id','rating','ts']
df1=pd.read_csv('u.data',sep='\t',names=col).drop('ts', axis=1)
col1=['movie-id','title'] + [str(i) for  i in range(22)]
df = pd.read_csv('u.item', sep= '|', names =col1, encoding = "ISO-8859-1")[['movie-id' , 'title']]

#Merge
Movie = pd.merge(df, df1, on='movie-id')
#Python Tkinter Frame widget is used to organize the group of widgets. It acts like a container which can be used to hold the other widgets.
frame=ttk.Frame(app)
frame.place(x=60,y=70)

result=ttk.Variable(app)

#Now we will be creating a Listbox 
box=ttk.Listbox(frame,height=20,width=80)#Here you can see the first argument is frame (meaning we need to box inside the paritcular frame)
for title in Movie["title"].unique():
    box.insert(ttk.END,title)

#This will  pack it inside the frame
box.pack(side='left',fill='y')

#We need a scroll bar a scrolling film names
scroll=ttk.Scrollbar(frame,orient=ttk.VERTICAL)#orient meaning do we need a vertical or horizontal scroll bar
scroll.config(command=box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right',fill='y')

#Creating Recommendation
def movie():
    movie_selected=box.get(box.curselection())
    print('Movie Selected :',movie_selected)


    #Creating a Pivot table
    movie_pivot=Movie.pivot_table(index='user-id', columns='title', values='rating')


    #Finding Similarities for movie
    corrs=movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df=pd.DataFrame(corrs,columns=['correlation'])
    corrs_df['rating']= Movie.groupby('title')['rating'].mean()
    corrs_df['count']=Movie['title'].value_counts()


    #Finding the Top most recommendation
    top_recom = list(corrs_df[corrs_df['count']>50].sort_values(by='correlation' , ascending = False).head(2).index)
    
    #Important
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)
    print('Recomendation :',top_recom)
    
    if top_recom:
        result.set(top_recom[0])
    else:
        result.set(top_recom[0])
    
    print('Recomendation :',top_recom)
    result.set(top_recom[0])

#Creating a button for top recommendation
ttk.Button(app,text='Find Recommendation',command=movie,font='arial').place(x=60,y=500)
ttk.Label(app,textvariable=result,font='Arial').place(x=60,y=540)



app.mainloop()