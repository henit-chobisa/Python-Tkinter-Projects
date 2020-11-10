from tkinter import *
window = Tk()
window.geometry("900x400")
def sur1():
    k = "Henit"
    lab1 = Label(text = k , font = "comicsansms 20 bold").pack(side = BOTTOM , anchor = "s")
def sur2():
    l = "Chobisa"
    lab2 = Label(text = l , font = "comicsansms 20 bold").pack(side = BOTTOM , anchor = "s")
def sur3():
    m = " is a good "
    lab3 = Label(text = m , font = "comicsansms 20 bold").pack(side = BOTTOM , anchor = "s")
def sur4():
    n = "Person"
    lab4 = Label(text = n, font = "comicsansms 20 bold").pack(side = BOTTOM , anchor = "s" )



bt1 = Button(text = "Surprise 1 " , fg = "blue", bg = "grey" ,font ="comicsansms 20 bold" , borderwidth = 3 , relief  = SUNKEN , command  = sur1)
bt1.pack(fill = X, padx = 30)
bt2 = Button(text = "Surprise 2 " , fg = "blue", bg = "grey" ,font ="comicsansms 20 bold" , borderwidth = 3 , relief  = SUNKEN , command = sur2)
bt2.pack(fill = X, padx = 30)
bt3 = Button(text = "Surprise 3 " , fg = "blue", bg = "grey" ,font ="comicsansms 20 bold" , borderwidth = 3 , relief  = SUNKEN , command = sur3)
bt3.pack(fill = X, padx = 30)
bt4 = Button(text = "Surprise 4 " , fg = "blue", bg = "grey" ,font ="comicsansms 20 bold" , borderwidth = 3 , relief  = SUNKEN , command = sur4)
bt4.pack(fill = X, padx = 30)
window.mainloop()