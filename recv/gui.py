#!/usr/bin/python
from tkinter import *
from PIL import ImageTk, Image


def refresh_image(canvas, img, image_path, image_id):
    try:
        pil_img = Image.open(image_path)
        img = ImageTk.PhotoImage(pil_img)
        canvas.itemconfigure(image_id, image=img)
    except IOError:  # missing or corrupt image file
        ##img = None
        print('No image')
    # repeat every half sec
    canvas.after(1, refresh_image, canvas, img, image_path, image_id)


root = Tk()
image_path = 'img.jpg'

canvas = Canvas(root, height=480, width=640)
img = None  # initially only need a canvas image place-holder
image_id = canvas.create_image(320, 240, image=img)
canvas.pack()

refresh_image(canvas, img, image_path, image_id)
root.mainloop()