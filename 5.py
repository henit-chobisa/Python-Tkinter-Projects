import cv2
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("900x600")

lab = Label(window)
cap = cv2.VideoCapture("c.mp4")
while True:
    imageget = cap.read()
    imagefetch = ImageTk.PhotoImage(image = imageget)
    lab.config(image = imagefetch)
    lab.image = imagefetch

lab.pack() 












window.mainloop()
'''vid = cv2.VideoCapture("c.mp4")
frame = vid.read()
frame = Image.fromarray(frame)
frame = PhotoImage(frame)
lab.configure(image = frame)
lab.image = frame
lab.pack()'''
