from tkinter import *
macw = Tk()
macw.geometry("900x400")
re = Label(text = "Ready", fg = "grey" , bg = "black" , font = "comicsansms 19 italic",borderwidth = 6, relief = SUNKEN)
def ent(e):
    re.config(text = "Let's go", fg = "Red" , bg = "grey" , font = "comicsansms 29 italic",borderwidth = 6, relief = SUNKEN)
def lea(k):
    re.config(text = "Come on man! CLICK ME", fg = "grey" , bg = "black" , font = "comicsansms 19 italic",borderwidth = 6, relief = SUNKEN)

re.bind("<Enter>",ent )
re.bind("<Leave>", lea)
re.pack(anchor = "se" , side = BOTTOM, fill = X , padx = 10 , pady = 10)
macw.mainloop()