import cv2
from tkinter import *
from PIL import Image, ImageTk

class Videostream:
    
    panel = None
    window = None
    camera = None
    def __init__(self):
        self.window = Tk()
        self.window.title("Magical Newspaper")
        self.window.geometry("900x400")
        self.panel= Label(self.window)
        self.panel.pack()
        self.camera=cv2.VideoCapture("c.mp4")
        self.camera1()
        self.window.mainloop()
    def camera1(self):
        _,frame=self.camera.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame=Image.fromarray(frame)
        frame=ImageTk.PhotoImage(frame)
        self.panel.configure(image = frame)
        self.panel.image=frame 
        #self.panel.after(1,self.camera)
if __name__ == '__main__':
    objVideo = Videostream()