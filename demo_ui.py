from PIL import Image, ImageTk
import customtkinter


def combobox_callback():
    print("button pressed")


app = customtkinter.CTk()
app.title("Poke Finder")
app.attributes('-topmost', True)

frame1 = customtkinter.CTkFrame(app)
frame2 = customtkinter.CTkFrame(app)

player = Image.open('player_idle.png').resize((40, 50))
player = ImageTk.PhotoImage(player)

pika = Image.open('pikachu.png').resize((50, 50))
pika = ImageTk.PhotoImage(pika)

player_label = customtkinter.CTkLabel(frame1, image=player, text='')
pika_label = customtkinter.CTkLabel(frame1, image=pika, text='')

place_var = customtkinter.StringVar()
place_var.set("Where are you")

name_var = customtkinter.StringVar()
name_var.set("Pokemon name")

result_var = customtkinter.StringVar()
result_var.set("location list: location 1, 2, 3")

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

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

app.mainloop()
