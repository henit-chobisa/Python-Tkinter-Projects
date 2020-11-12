from tkinter import *
import math
window =Tk()
window.geometry("900x400")
window.title("LOADING WINDOW")
can = Canvas(width = 900, height = 400 , bg = "black")
while True:
    for x in range (450,551):
        x = x+1
        y1 = (200 + math.sqrt(20100 - ((x - 450)*(x - 450))))
        y2 = (200 - math.sqrt(20100 - ((x - 450)*(x - 450))))
        y1 = int(y1)
        y2 = int(y2)
        can.create_line(450,200,x,y1,fill = "red")
        can.create_line(450,200,x,y2,fill = "red")



can.pack(fill = BOTH)






window.mainloop()