from tkinter import *

users = []
passwords = []
window = Tk()
window.geometry("900x400")
window.config(bg = "black")
lb1 = Label(text = " Hi there, Please log in down here " , font = "comicsansms 20 italic" , fg = "Red", bg = "Black" , borderwidth  = 7, relief  =SUNKEN )
lb1.pack(fill = X , pady = 10)
k = StringVar()
l = StringVar()
tex1  = Label( text = "USERNAME :  " , fg = "white" , bg = "black", font = "comicsansms 13 italic")
tex1.pack(side = TOP)
usrn = Entry(textvariable = k).pack(side = TOP , fill = X , padx =200)
tex2  = Label( text = "PASSWORD :  " , fg = "white" , bg ="black", font = "comicsansms 13 italic")
tex2.pack(side = TOP)
uspa = Entry(textvariable = l).pack(side = TOP , fill = X , padx = 200)
def get():
    username = k.get()
    userpass = l.get()
    users.append(k)
    passwords.append(l)
    with open("records.txt", "a") as f:
        f.write("{}   {}\n".format(username ,userpass))

    root = Tk()
    root.title("Thanks")
    mess = Label(root, text = "Thanks for subbmission. INDEX NUMBER :{} ".format(users.index(k)), fg = "green", bg = "black" , borderwidth = 2 ,relief = SUNKEN , font = "cosmicsansserif 15 italic").pack()
    root.mainloop()
    print(users)
    print(passwords)
    print(users)


bt = Button(text = "Please Submit" , font = "comicsansms 17 bold italic", fg = "red" , bg= "grey" , command = get)
def ent(e):
    bt.config(text = "Yes!! Yes!! CLICK", font = "comicsansms 17 bold italic", fg = "red" , bg= "grey")
def lea(e):
    bt.config(text = "Please Submit", font = "comicsansms 17 bold italic", fg = "red" , bg= "grey")


bt.bind("<Enter>" , ent)
bt.bind("<Leave>" , lea)
bt.pack(side = TOP , pady =20)
print(users)

window.mainloop()