from tkinter import *
window = Tk()
window.title("Window Resizer")
window.geometry("900x400")
k = StringVar()
l = StringVar()

def get():
    p = k.get()
    q = l.get()
    window.geometry(f"{p}x{q}")

tit = Label(text = "Resize your window" , font = "comicsansms 20 italic").pack(fill = BOTH , pady = 20)
wid = Label(text = "ENTER THE WIDTH BELOW").pack(fill = BOTH)
wident = Entry(textvariable = k).pack()
hei = Label(text = "ENTER THE height BELOW").pack(fill = BOTH)
heient = Entry(textvariable = l).pack()

subm = Button(text = "APPLY" , command = get ).pack(pady = 30)





window.mainloop()
