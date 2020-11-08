from tkinter import *
from PIL import ImageTk , Image
import cv2


window = Tk()
window.geometry("1920x900")
window.minsize(1920,900)
imageget = Image.open("henit.jpg")
imageget = imageget.resize((300,300), Image.ANTIALIAS)
imagefetch = ImageTk.PhotoImage(imageget) 

lab = Label(image = imagefetch , bg = "grey" , borderwidth = 6)
'''def ente(e):
    cap = cv2.VideoCapture("c.mp4")
    while True:
        success, img = cap.read()  
        #cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
        lab.config(image= cv2.imshow("Image",img))'''

lab.pack(side = LEFT, anchor ="nw" ,padx = 10, pady = 10)
window.mainloop()