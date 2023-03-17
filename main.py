from tkinter import *; hex_rgb = input("HEX or RGB?(1/2): "); possibilites = ["1", "2"]
def rgb(r, g,b):return "#%02x%02x%02x" % (r, g, b)
if hex_rgb in possibilites:
    if hex_rgb == possibilites[0]: bgcolor = input("HEX Code?: ");root = Tk();root.title("Preview");root.configure(background=bgcolor);root.mainloop()
    else:base = input("RGB Code?: ");inputs = base.split(",");bgcolor = rgb(int(inputs[0]), int(inputs[1]), int(inputs[2]));root = Tk();root.title("Preview");root.configure(background=bgcolor);root.mainloop()
