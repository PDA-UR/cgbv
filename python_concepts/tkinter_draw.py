#!/usr/bin/env python3
# check https://tkdocs.com/ for documentation

import tkinter

window = tkinter.Tk(className="bla")
canvas = tkinter.Canvas(window, width=400, height=400, background='white')
canvas.pack()


def on_mouse_down(event):
    # print("down at: ", event.x, event.y)
    # canvas.create_line(start_x, start_y, event.x, event.y, fill='red', width=3)
    canvas.create_rectangle(event.x, event.y, event.x, event.y)


def on_mouse_up(event):
    # print("up at: ", event.x, event.y)
    pass


def on_mouse_drag(event):
    # print("move at: ", event.x, event.y)
    canvas.create_rectangle(event.x, event.y, event.x, event.y)


# see https://python-course.eu/tkinter_events_binds.php for more events
canvas.bind("<Button-1>", on_mouse_down)
canvas.bind("<ButtonRelease-1>", on_mouse_up)
canvas.bind("<B1-Motion>", on_mouse_drag)
tkinter.mainloop()
