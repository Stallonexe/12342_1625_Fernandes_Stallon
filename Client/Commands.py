import hashlib
from tkinter import messagebox
from Client import *



def HashPassword(UserPassword, RepeatPassword, UserSalt):
    if UserPassword == RepeatPassword:
        password = UserSalt + UserPassword
        HashedPassword = hashlib.sha256(password.encode())
        return HashedPassword.hexdigest()
    else:
        messagebox.showerror("Registration Failed", "The passwords do not match.")


def Register(Email_Entry, Name_Entry, Surname_Entry, Contact_Entry, Password_Entry, RepeatPassword_Entry ):
    Email = Email_Entry.get()
    Name = Name_Entry.get()
    Surname = Surname_Entry.get()
    ContactNo = Contact_Entry.get()

    UserPassword = Password_Entry.get()
    RepeatPassword = RepeatPassword_Entry.get()

    #UserSalt = Salt_Generator.gen_hex()

    UserSalt = "asdghj"

    HashedPassword = HashPassword(UserPassword, RepeatPassword, UserSalt)

    #print(Email, Name, Surname, ContactNo, UserSalt, HashedPassword)
    if HashedPassword:
        Send(f"!Register {Email} {UserSalt} {HashedPassword} {Name} {Surname} {ContactNo}")
        Send(DISCONNECT_MESSAGE)
    else:
        pass



def Login(Email_Entry, Password_Entry):
    Email = Email_Entry.get()
    Password = Password_Entry.get()

    #Get hash
    
#Server sends True if registerd and false if not.

# The client will be in while loop, waiting for the reply, while reply is true, it will move to next screen