import pandas as pd
import seaborn as sns
import matplotlib as plt

from PIL import Image, ImageTk
import customtkinter


def combobox_callback():
    print("button pressed")


app = customtkinter.CTk()
app.title("Poke Finder")

frame1 = customtkinter.CTkFrame(app)
frame2 = customtkinter.CTkFrame(app)

player = Image.open('player_idle.png')
player = customtkinter.CTkImage(light_image=player, size=(80, 100))

pika = Image.open('pikachu.png')
pika = customtkinter.CTkImage(light_image=pika, size=(100, 100))

player_label = customtkinter.CTkLabel(frame1, image=player, text='')
pika_label = customtkinter.CTkLabel(frame1, image=pika, text='')

place_var = customtkinter.StringVar()
place_var.set("Where are you")

name_var = customtkinter.StringVar()
name_var.set("Pokemon name")

result_var = customtkinter.StringVar()
result_var.set("Closest Path: A->B->C->Destination")

place_butt = customtkinter.CTkComboBox(frame1, variable=place_var)
name_butt = customtkinter.CTkComboBox(frame1, variable=name_var)

result_label = customtkinter.CTkEntry(frame2, textvariable=result_var)

player_label.grid(row=0, column=0)
pika_label.grid(row=0, column=1)
place_butt.grid(row=1, column=0, padx=20, pady=20, sticky='NEW')
name_butt.grid(row=1, column=1, padx=20, pady=20, sticky='NEW')
frame1.grid_columnconfigure((0, 1), weight=1)
frame1.rowconfigure(1, weight=1)

result_label.grid(row=0, column=0, sticky='NSEW')
frame2.grid_columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

frame1.pack(fill='x', expand=False)
frame2.pack(fill='both', expand=True)

app.mainloop()
