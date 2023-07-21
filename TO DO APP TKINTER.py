from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("To-Do-App")#To initialize tkinter, we have to create a Tk root widget, which is a window with a title bar and other decoration provided by the window manage
root.iconbitmap('c:/Users/haide/Immerse/ticker.ico')
root.geometry("500x800")
root.resizable(False, False)
root.config(background = "sky blue")

my_font = Font(
    family="Arial Rounded MT Bold",
    size=10,
    weight="normal")

def multi_yview(*args):
    my_list.yview(*args)
    time_list.yview(*args)

my_frame = Frame(root, width=500, height=800, background="sky blue")#organize the group of widgets. It acts like a container which can be used to hold the other widgets.
my_frame.pack(pady=0)

title = Label(my_frame, text="Ticker", bg="sky blue", fg="white", font=("Arial Rounded MT Bold", 50, "bold"))
title.pack(side=TOP, pady=20)

list_frame = Frame(root)
list_frame.pack(pady=20)

my_list = Listbox(list_frame,
                  font=my_font,
                  width=20,
                  height=15,
                  #bg="SystemButtonFace",
                  bd=0,
                  bg="LightSteelBlue1",
                  fg="Navy",
                  activestyle="none",
                  selectbackground="light slate blue"

                  )

time_list = Listbox(list_frame,
                  font=my_font,
                  width=20,
                  height=15,
                  #bg="SystemButtonFace",
                  bd=0,
                  bg="LightSteelBlue1",
                  fg="Navy",
                  activestyle="none",
                  selectbackground="light slate blue"

                    )

my_list.pack(side=LEFT)
time_list.pack(side=RIGHT, padx=5)
#my_scrollbar.grid(row=0, column=2)

#my_list.config(yscrollcommand=my_scrollbar.set)

#Dummy list
stuff = ("Walk the dog", "Do groceries", "Eat lunch","Carry","On","Live","I","See","Crystal")
time_stuff = ("1:00", "2:00", "3:00","4:00","5:00","6:00","7:00","8:00","9:00")


#Add dummy list to list box
for item in stuff:
    my_list.insert(END, item)
for item in time_stuff:
    time_list.insert(END, item)


def my_temp_text(e):
   my_entry.delete(0,"end")

def time_temp_text(e):
   time_entry.delete(0,"end")


my_entry = Entry(root, font=("Arial", 15), fg="grey63")
my_entry.insert(0, "Enter task")
my_entry.pack(pady=10)
my_entry.bind("<FocusIn>", my_temp_text)

time_entry = Entry(root, font=("Arial", 15,), fg="grey63")
time_entry.insert(0, "Enter time")
time_entry.pack(pady=10)
time_entry.bind("<FocusIn>", time_temp_text)


#Buttons frame
button_frame = Frame(root)
button_frame.pack(pady=20)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)
    time_list.insert(END, time_entry.get())
    time_entry.delete(0,END)

def delete_item():
    for item in my_list.curselection():
        point = item
    print (point)
    my_list.delete(ANCHOR)
    time_list.delete(point)

def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="gray34")
    my_list.select_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="White")
    my_list.select_clear(0, END)


add_button = Button(button_frame, text="Add task", command=add_item)
delete_button = Button(button_frame, text="Delete task", command=delete_item)
cross_button = Button(button_frame, text="Tick", command=cross_item)
uncross_button = Button(button_frame, text="Untick", command=uncross_item)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)

root.mainloop()