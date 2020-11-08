from tkinter import *
root = Tk()
#widthxheight
root.geometry("900x400")
root.minsize(900,400)
root.maxsize(900,400)
Text  = Label(text = "Henit is a very good person" , fg = "red" )
Text.pack()
root.mainloop()