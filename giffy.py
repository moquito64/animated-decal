""" Uses tkinter to create a frame and play an asset file """
from tkinter import *
from PIL import ImageTk, Image
#import time
#import os
root = Tk(className = '- Digital Monster -')
root.geometry("240x320")

FRAMECNT = 4
GM_FILE = 'assets/greymon-scaled.gif'

frames = [PhotoImage(file=GM_FILE,format = f'gif -index {i}') for i in range(FRAMECNT)]


def update(ind):
    """ Keep the frame up to date """
    frame = frames[ind]
    ind += 1
    if ind == FRAMECNT:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
label.config(bg="#24201b")
root.after(0, update, 0)
root.mainloop()
