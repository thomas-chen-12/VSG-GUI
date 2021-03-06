"""
Example program (exercise) for GUI in Python
"""
from tkinter import *
import tkinter.messagebox as messagebox
import os.path

canvas = None
LIGHT_GREEN = "#CDEA90"         # TKinter does not support shapes with transparant colors. Use create_image() and attach a PNG file instead.

def exit_warning():
    answer = messagebox.askquestion("Exit VSG", "Are you sure you want to exit the program?")
    if answer == "yes":
        quit()
    else:
        return

def foo():
    print("Welcome to the best project in Capstone Expo")

def show_message_box(title, message):
    messagebox.showinfo(title, message)

def magic():
    canvas.delete(green_box)

# Set the window title and size
root = Tk()
root.title("Vector Signal Generator (Beta)")
root.geometry("1280x720")
root.resizable(True, True)

# Add main menu and its sub-menus to the root
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=False)
instrument_menu = Menu(main_menu, tearoff=False)
file_menu.add_command(label="New Project", command=foo)
file_menu.add_command(label="Save", command=foo)
file_menu.add_command(label="Save As...", command=foo)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_warning)
instrument_menu.add_command(label="Add Instrument", command=foo)
instrument_menu.add_command(label="Find Instrument", command=foo)
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Instrument", menu=instrument_menu)

# Add toolbar to the root
toolbar = Frame(root, bg="blue")
btn_insert = Button(toolbar, text="Insert Something", command=lambda:show_message_box("Hi", "Yikes"))
btn_insert.pack(side=LEFT, padx=5, pady=5)
btn_print = Button(toolbar, text="Print", command=foo)
btn_print.pack(side=LEFT, padx=5, pady=5)
btn_magic = Button(toolbar, text="Magic", command=magic)
btn_magic.pack(side=LEFT, padx=5, pady=5)
toolbar.pack(side=TOP, fill=X)

# Add status bar
# 'bg' stands for background. Make it SUNKEN. Anchor the text to left (West)
status_bar = Label(root, text="Bored", bd=True, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

# Add canvas for shapes and graphics
canvas = Canvas(root, width=640, height=360)
canvas.pack()
black_line = canvas.create_line(0,0, 640, 360)
red_line = canvas.create_line(0, 360, 640, 0, fill="red")
green_box = canvas.create_rectangle(160, 90, 480, 270, fill=LIGHT_GREEN)

# Add meme
meme = PhotoImage(file=os.path.join(os.path.dirname(os.path.realpath(__file__)), "img","meme.png"))
label_meme = Label(root, image=meme)
label_meme.pack()

root.mainloop()