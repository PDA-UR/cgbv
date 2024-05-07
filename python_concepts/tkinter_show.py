import tkinter
from PIL import ImageDraw, Image, ImageTk
import sys

window = tkinter.Tk(className="Show")

image = Image.open(sys.argv[1])
image = image.resize((1000, 800), Image.LANCZOS)
canvas = tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)

canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)


def callback(event):
    print("clicked at: ", event.x, event.y)


canvas.bind("<Button-1>", callback)
tkinter.mainloop()
