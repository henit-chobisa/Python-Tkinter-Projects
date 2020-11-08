from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("900x400")
window.title("Hover Project")
lab = Label(text = "Hi there hover me ", fg =  "white", bg = "black")
def hov(e):
    lab.config(text = "Hover", fg = "Black", bg = "white")
def lea(K):
    lab.config(text = "Hi there hover over me ", fg =  "white", bg = "black")



lab.bind("<Enter>",hov)
lab.bind("<Leave>",lea) 
lab.pack()



window.mainloop()