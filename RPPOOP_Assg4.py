from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")

# Menubar:
def show_msg(item):
    messagebox.showinfo("Information", f"You clicked {item}")
   
menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New", command=lambda: show_msg("New"))
menu1.add_command(label="Open", command=lambda: show_msg("Open"))
menu1.add_command(label="Save", command=lambda: show_msg("Save"))
menu1.add_command(label="Save as..", command=lambda: show_msg("Save as.."))
menu1.add_separator()
menu1.add_command(label="Quit", command=root.quit)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Item1B", command=lambda: show_msg("Item1B"))
menu2.add_separator()
menu2.add_command(label="Item2B", command=lambda: show_msg("Item2B"))
menu2.add_command(label="Item3B", command=lambda: show_msg("Item3B"))
menu2.add_command(label="Item4B", command=lambda: show_msg("Item4B"))
menu2.add_command(label="Item5B", command=lambda: show_msg("Item5B"))

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Item1C", command=lambda: show_msg("Item1C"))
menu3.add_command(label="Item2C", command=lambda: show_msg("Item2C"))

menubar.add_cascade(label="Menu1", menu=menu1)
menubar.add_cascade(label="Menu2", menu=menu2)
menubar.add_cascade(label="Menu3", menu=menu3)

root.config(menu=menubar)

# Labels:
var1 = StringVar()
var1.set("This is label 1")
label1 = Label(root, textvariable=var1, bg="yellow", relief=GROOVE)
label1.pack(pady=10)

var2 = StringVar()
var2.set("This is label 2")
label2 = Label(root, textvariable=var2, bg="cyan", relief=GROOVE)
label2.pack(pady=10)

colors = ["yellow", "green", "blue", "red", "cyan", "magenta", "pink", "purple", "orange", "brown", "beige", "turquoise", "navy", "salmon", "lavender"]


label_var = StringVar()
label_var.set("Label 1")
label_dropdown = OptionMenu(root, label_var, "Label 1", "Label 2")
label_dropdown.pack(pady=10)

color_var = StringVar()
color_var.set(colors[0])
color_dropdown = OptionMenu(root, color_var, *colors)
color_dropdown.pack(pady=10)


def change_label_color():
    if label_var.get() == "Label 1":
        label1.config(bg=color_var.get())
    elif label_var.get() == "Label 2":
        label2.config(bg=color_var.get())

change_button = Button(root, text="Change color", command=change_label_color)
change_button.pack(pady=10)

root.mainloop()
