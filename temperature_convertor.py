import tkinter as tk
from tkinter import LabelFrame, Button, Entry


gui = tk.Tk()

gui.title("Temperature Convertor App")
gui.geometry("530x300")

celsius_label_frame = LabelFrame(gui, text="Celsius to Fahrenheit")
fahrenheit_label_frame = LabelFrame(gui, text="Fahrenheit to Celsius")

celsius_entry = Entry(celsius_label_frame, width=10, state="readonly")
celsius_entry.place(x=45, y=25)

fahrenheit_entry = Entry(fahrenheit_label_frame, width=10, state="readonly")
fahrenheit_entry.place(x=45, y=25)

celsius_label_frame.place(x=50, y=60, height=100, width=180)
fahrenheit_label_frame.place(x=300, y=60, height=100, width=180)


def activate_celsius_entry():
    if celsius_entry['state'] == "normal":
        celsius_entry.config(state="disabled")
    else:
        celsius_entry.config(state="normal")


def activate_fahrenheit_entry():
    if fahrenheit_entry['state'] == "normal":
        fahrenheit_entry.config(state="disabled")
    else:
        fahrenheit_entry.config(state="normal")

activate_celsius_btn = Button(gui, text="Activate C to F", command=activate_celsius_entry)
activate_celsius_btn.place(x=80, y=170)

activate_fahrenheit_btn = Button(gui, text="Activate F to C", command=activate_fahrenheit_entry)
activate_fahrenheit_btn.place(x=330, y=170)

convert_button = Button(gui, text="Convert")
convert_button.place(x=130, y=240)

results_entry = Entry(gui, bg="green", width=10)
results_entry.place(x=220, y=240)

clear_button = Button(gui, text="Clear")
clear_button.place(x=340, y=240)

exit_button = Button(gui, text="Exit", command=gui.destroy)
exit_button.place(x=440, y=240)

gui.mainloop()
