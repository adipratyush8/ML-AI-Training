from turtle import window_height
import pandas as pd
import tkinter as ttk
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
from PIL import Image,ImageTk
 
app=ttk.Tk()
app.geometry('600x600')
app.title('Canvas')

#Creating a Canvas
canvas=ttk.Canvas(app,width=400,height=400)
canvas.pack()

#Loading an Image in the script

img=ImageTk.PhotoImage(Image.open('graph.png'))

#Add image to the canvas Items
canvas.create_image(10,10,anchor=ttk.NW,image=img)

app.mainloop()