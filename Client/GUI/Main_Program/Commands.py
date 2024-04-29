import hashlib
from tkinter import messagebox
import Salt_Generator



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

    UserSalt = Salt_Generator.gen_hex()

    HashedPassword = HashPassword(UserPassword, RepeatPassword, UserSalt)

    print(Email, Name, Surname, ContactNo, UserSalt, HashedPassword)
    #Login_database.register(UserEmail, UserSalt, PasswordHash, FirstName, Surname, ContactNo)

