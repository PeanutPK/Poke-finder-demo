import tkinter as tk

from PIL import Image, ImageTk
import customtkinter


def combobox_callback():
    print("button pressed")


app = customtkinter.CTk()
app.title("Poke Finder")

player = Image.open('player_idle.png')
player = ImageTk.PhotoImage(player)

pika = Image.open('pikachu.png')
pika = ImageTk.PhotoImage(pika)

player_label = customtkinter.CTkLabel(app, image=player, text='')
pika_label = customtkinter.CTkLabel(app, image=pika, text='')

place_var = customtkinter.StringVar()
place_var.set("Where are you")

name_var = customtkinter.StringVar()
name_var.set("Pokemon name")

place_butt = customtkinter.CTkComboBox(app, variable=place_var)
name_butt = customtkinter.CTkComboBox(app, variable=name_var)

player_label.grid(row=0, column=0)
pika_label.grid(row=0, column=1)
place_butt.grid(row=1, column=0, padx=20, pady=20)
name_butt.grid(row=1, column=1, padx=20, pady=20)


app.mainloop()
