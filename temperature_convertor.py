import tkinter as tk
from tkinter import LabelFrame, Button, Entry, END, messagebox


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


def clear_fields():
    celsius_entry.delete(0, END)
    fahrenheit_entry.delete(0, END)
    results_entry.delete(0, END)


def temperature_conversion():

    if celsius_entry['state'] == "normal" and celsius_entry.get() != "":
        to_fahrenheit = float(celsius_entry.get()) * 9/5 + 32
        results_entry.delete(0, END)
        results_entry.insert(0, to_fahrenheit)
    elif fahrenheit_entry['state'] == "normal" and fahrenheit_entry.get() != "":
        to_celsius = (float(fahrenheit_entry.get()) - 32) * 5/9
        results_entry.delete(0, END)
        results_entry.insert(0, to_celsius)
    else:
        return None


def exit_program():
    msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application", icon='warning')
    if msg_box == "yes":
        gui.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")

def activate_celsius_entry():
    if celsius_entry['state'] == "normal":
        celsius_entry.config(state="disabled")
    else:
        celsius_entry.config(state="normal")
        fahrenheit_entry.config(state="disabled")


def activate_fahrenheit_entry():
    if fahrenheit_entry['state'] == "normal":
        fahrenheit_entry.config(state="disabled")
    else:
        fahrenheit_entry.config(state="normal")
        celsius_entry.config(state="disabled")


activate_celsius_btn = Button(gui, text="Activate C to F", command=activate_celsius_entry)
activate_celsius_btn.place(x=80, y=170)

activate_fahrenheit_btn = Button(gui, text="Activate F to C", command=activate_fahrenheit_entry)
activate_fahrenheit_btn.place(x=330, y=170)

convert_button = Button(gui, text="Convert", command=temperature_conversion)
convert_button.place(x=130, y=240)

results_entry = Entry(gui, bg="green", width=10)
results_entry.place(x=220, y=240, height=29.5)

clear_button = Button(gui, text="Clear", command=clear_fields)
clear_button.place(x=340, y=240)

exit_button = Button(gui, text="Exit", command=exit_program)
exit_button.place(x=440, y=240)

gui.mainloop()
