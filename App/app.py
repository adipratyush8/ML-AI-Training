import os
from numpy import place
import tkinter as ttk
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
print('location is: ', os.getcwd(), '/n/n/n/n')

app = ttk.Tk()
app.title('Movie Recommendation')
app.geometry('700x700')

cols = ['user_id', 'movie_id', 'rating', 'ts']
df = pd.read_csv('u.data', sep='\t', names=cols).drop('ts', axis=1)
item_cols = ['movie_id', 'title'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep='|', names=item_cols,
                  encoding="ISO-8859-1")[['movie_id', 'title']]
movie = pd.merge(df, df1, on='movie_id')

ttk.Label(app, text='Movie Recommendation',
          font=('Algerian', 15)). place(x=280, y=5)
result = ttk.Variable(app)

frame = ttk.Frame(app)
frame.place(x=15, y=30)


box = ttk.Listbox(frame, height=15, width=45)
for title in movie['title'].unique():
    box.insert(ttk.END, title)

# box.grid(row=0 , column = 0)
box.pack(side='left', fill='y')

# box.place(x=10 , y=10)

scroll = ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(command=box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right', fill='y')


def get_movie():
    movie_selected = box.get(box.curselection())
    print('movie selected: ', movie_selected)

    # create pivot table
    movie_pivot = movie.pivot_table(
        index='user_id', columns='title', values='rating')

    # find similarities for selected movie
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df = pd.DataFrame(corrs, columns=['correltion'])
    corrs_df['rating'] = movie.groupby('title')['rating'].mean()
    corrs_df['count'] = movie['title'].value_counts()

    # find top 2-3 recommendation
    top_recom = list(corrs_df[corrs_df['count'] > 50].sort_values(
        by='correltion', ascending=False).head(3).index)

    # IMPORTANT
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)
    print('Recommendations: ', top_recom)

    if top_recom:
        result.set(top_recom[0])

    else:
        result.set(top_recom[0])

    print('recommendations: ', top_recom)

    result.set(top_recom[0])


ttk.Button(app, text='Find recommendation', command=get_movie,
           font=('Arial', 22)).place(x=15, y=280)
ttk.Label(app, textvariable=result, font=('arial', 22)).place(x=10, y=350)


app.mainloop()
