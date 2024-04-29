import tkinter as Tk
import hashlib
from tkinter import messagebox
from tkinter import PhotoImage
from Main_Program.Commands import *

from tkinter import font
#from Database import Login_database
#from Algorithms.Login import Salt_Generator
#from Algorithms.Login import mergesort
#from Algorithms.Login.Salt_Generator import gen_hex

#https://www.theappfuel.com/examples/discord_onboarding

window = Tk.Tk()
window.title("Welcome to Housify")
window.geometry('450x800')
#window.resizable(False, False)

bg_image = PhotoImage(file='Images/Background/Welcome.png')
bg_label = Tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)






def EntryScreen():
    bg_label = Tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    EntryFrame = Tk.Frame(window, bg='#222222')

    #Create Widgets
    Register_button = Tk.Button(EntryFrame, text="Register", bg='#1aebff', fg="Black", font=("Arial", 16), height= 1, width=33,
                                command=lambda: RegisterScreen(EntryFrame))


    Login_button = Tk.Button(EntryFrame, text="Login", bg='#575757', fg="white", font=("Arial", 16), height= 1, width=33,
                             command=lambda: LoginScreen(EntryFrame))

    # Grid Layout for widgets
    Register_button.grid(row=0, column=0, columnspan=2, pady=0)
    Login_button.grid(row=1, column=0, columnspan=2, pady=(25,50))

    EntryFrame.pack(side='bottom')

def RegisterScreen(EntryFrame):
    EntryFrame.destroy()
    bg_label.destroy()

    # Creating Widgets
    RegisterFrame = Tk.Frame(window, bg='#222222')
    Back_Button = Tk.Button(RegisterFrame, text="◄  Back", bg='#222222', fg="white", font=("Arial", 14),
                            command=lambda: (RegisterFrame.destroy(), EntryScreen()), borderwidth=0)
    Register_label = Tk.Label(RegisterFrame, text="Register", bg='#222222', fg="white", font=("Arial", 20, 'bold'))


    Name_Label = Tk.Label(RegisterFrame, text="Name",  bg='#222222', fg="white", font=("Arial", 16))
    Name_Entry = Tk.Entry(RegisterFrame, font=("Arial", 16))

    Surname_Label = Tk.Label(RegisterFrame, text="Surname", bg='#222222', fg="white", font=("Arial", 16))
    Surname_Entry = Tk.Entry(RegisterFrame, font=("Arial", 16))

    Contact_Label = Tk.Label(RegisterFrame, text="Contact Number", bg='#222222', fg="white", font=("Arial", 16))
    Contact_Entry = Tk.Entry(RegisterFrame, font=("Arial", 16))

    Email_Label = Tk.Label(RegisterFrame, text="Email Address", bg='#222222', fg="white", font=("Arial", 16))
    Email_Entry = Tk.Entry(RegisterFrame, font=("Arial", 16))

    # Password
    Password_Label = Tk.Label(RegisterFrame, text="Password", bg='#222222', fg="white", font=("Arial", 16))
    Password_Entry = Tk.Entry(RegisterFrame, show="*", font=("Arial", 16))

    # Repeat Password
    RepeatPassword_Label = Tk.Label(RegisterFrame, text="Repeat Password", bg='#222222', fg="white", font=("Arial", 16))
    RepeatPassword_Entry = Tk.Entry(RegisterFrame, show="*", font=("Arial", 16))

    Register_button = Tk.Button(RegisterFrame, text="Register", bg='#1aebff', fg="Black", font=("Arial", 16),
                                command=lambda: Register(Email_Entry, Name_Entry, Surname_Entry, Contact_Entry, Password_Entry, RepeatPassword_Entry))

    #Adding Widget
    Back_Button.grid(row=0, column=0, columnspan=2, padx=5, pady=25, sticky="w")
    Register_label.grid(row=1, column=0, columnspan=2, padx=168)

    Name_Label.grid(row=2, column=0, padx=(50,0), pady=(25,0), sticky="w")
    Name_Entry.grid(row=3, column=0, columnspan=2, padx=50, sticky="ew")

    Surname_Label.grid(row=4, column=0, padx=(50,0), pady=(25,0), sticky="w")
    Surname_Entry.grid(row=5, column=0, columnspan=2, padx=50, sticky="ew")

    Contact_Label.grid(row=6, column=0, padx=(50,0), pady=(25,0), sticky="w")
    Contact_Entry.grid(row=7, column=0, columnspan=2, padx=50, sticky="ew")

    Email_Label.grid(row=8, column=0, padx=(50,0), pady=(25,0), sticky="w")
    Email_Entry.grid(row=9, column=0, columnspan=2, padx=50, sticky="ew")

    #Password 1
    Password_Label.grid(row=10, column=0, padx=(50, 0), pady=(25, 0), sticky="w")
    Password_Entry.grid(row=11, column=0, columnspan=2, padx=50, sticky="ew")

    #Password2
    RepeatPassword_Label.grid(row=12, column=0, padx=(50, 0), pady=(25, 0), sticky="w")
    RepeatPassword_Entry.grid(row=13, column=0, columnspan=2, padx=50, sticky="ew")

    #Register Button
    Register_button.grid(row=14, column=0, columnspan=2, padx=150, pady=50, sticky="ew")

    RegisterFrame.pack(fill=Tk.BOTH, expand=True)


def LoginScreen(EntryFrame):
    EntryFrame.destroy()
    bg_label.destroy()

    # Creating Widgets
    LoginFrame = Tk.Frame(window, bg='#222222')
    Back_Button = Tk.Button(LoginFrame, text="◄  Back", bg='#222222', fg="white", font=("Arial", 14),
                            command=lambda: (LoginFrame.destroy(), EntryScreen()), borderwidth=0)

    Login_Label = Tk.Label(LoginFrame, text="Login", bg='#222222', fg="white", font=("Arial", 20, 'bold'))

    #Email
    Email_Label = Tk.Label(LoginFrame, text="Email", bg='#222222', fg="white", font=("Arial", 16))
    Email_Entry = Tk.Entry(LoginFrame, font=("Arial", 16))

    #Password
    Password_Label = Tk.Label(LoginFrame, text="Password", bg='#222222', fg="white", font=("Arial", 16))
    Password_Entry = Tk.Entry(LoginFrame, show="*", font=("Arial", 16))

    Login_Button = Tk.Button(LoginFrame, text="Login", bg='#1aebff', fg="Black", font=("Arial", 16))


    #Placing Widgets
    Back_Button.grid(row=0, column=0, columnspan=2, padx=5, pady=25, sticky="w")
    Login_Label.grid(row=1, column=0, columnspan=2, padx=180)

    #Email
    Email_Label.grid(row=2, column=0, padx=(50, 0), pady=(25, 0), sticky="w")
    Email_Entry.grid(row=3, column=0, columnspan=2, padx=50, sticky="ew")

    #Password
    Password_Label.grid(row=4, column=0, padx=(50, 0), pady=(25, 0), sticky="w")
    Password_Entry.grid(row=5, column=0, columnspan=2, padx=50, sticky="ew")

    #Feature suggestion, remember me.

    # Login Button
    Login_Button.grid(row=6, column=0, columnspan=2, padx=150, pady=50, sticky="ew")







    LoginFrame.pack(fill=Tk.BOTH, expand=True)

EntryScreen()

window.mainloop()