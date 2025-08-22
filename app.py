import customtkinter as ctk
from PIL import Image
import os
from pets import get_random_dog


ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


app = ctk.CTk()
app.geometry("670x500")
app.title("Dog Image Generator")
app.resizable(False, False)


app.columnconfigure(0,weight=1)
app.columnconfigure(1,weight=10)
app.rowconfigure(0,weight=1)

def option_menu(choice):
    ctk.set_appearance_mode(choice.lower())

def theme_option_menu(choice):
    ctk.set_default_color_theme(choice)


def generateImg():
    get_random_dog()
    image_path = os.path.dirname(__file__)
    pet_image = ctk.CTkImage(Image.open(os.path.join(image_path, "pet.jpg")), size=(400,440))

    PetImageLabel = ctk.CTkLabel(master=PetImageFrame, image=pet_image,text='')
    PetImageLabel.grid(sticky='nsew',pady=10,padx=10)


LeftMenuFrame = ctk.CTkFrame(master=app)
LeftMenuFrame.grid(row=0,column=0,sticky="nsw")

LeftMenuFrame.rowconfigure(0, weight=0)  # for title
LeftMenuFrame.rowconfigure(1, weight=1)  #for option menu

Title = ctk.CTkLabel(master=LeftMenuFrame,text="Title",font=("Roboto",24))
Title.grid(row=0,column=0,pady=30,padx=80)


Button = ctk.CTkButton(master=LeftMenuFrame,text="Generate",command=generateImg)
Button.grid(row=1,column=0,sticky='s',pady=60)

ThemeOption = ctk.CTkOptionMenu(master=LeftMenuFrame,values=
                           ["Blue",
                            "Green",
                            "Dark-Blue"],
                            command=theme_option_menu)
ThemeOption.grid(row=2,column=0,sticky="s")

Option = ctk.CTkOptionMenu(master=LeftMenuFrame,values=
                           ["System",
                            "Light",
                            "Dark"],
                            command=option_menu)

Option.grid(row=3,column=0,sticky="s",pady=50)


PetImageFrame = ctk.CTkFrame(master=app)
PetImageFrame.grid(row=0,column=1,sticky="nsew",pady=20,padx=20)


app.mainloop()
