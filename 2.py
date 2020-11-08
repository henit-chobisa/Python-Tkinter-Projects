from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.geometry("350x198")
#photo = PhotoImage(file = "A.png")
image = Image.open("henit.jpg")
photo = ImageTk.PhotoImage(image) 
lab = Label(image=photo).pack()
window.mainloop()
