from tkinter import *
window = Tk()
window.title("Learn Canvas")
window.geometry("900x400")
can = Canvas(width = 900, height = 400)
can.create_rectangle(0,0,900,400,fill = "black" )
can.pack(fill = Y)


window.mainloop()
