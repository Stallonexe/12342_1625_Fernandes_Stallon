import sqlite3

class User:
    def __init__(self, UserEmail, UserSalt, Password, FirstName, Surname, ContactNo):

        #Attributes
        self.Email = UserEmail
        self.Salt = UserSalt
        self.Password = Password
        self.Name = FirstName
        self.Surname = Surname
        self.ContactNo = int(ContactNo)

        #Database
        self.connection = sqlite3.connect('login.db')
        self.cursor = self.connection.cursor()

        #Methods
        #self.CreateUserTable()
        self.RegisterUser()

    def CreateUserTable(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS UserTable
                              (
                              UserEmail VARCHAR(320) PRIMARY KEY NOT NULL,
                              UserSalt CHAR(6) NOT NULL,
                              PasswordHash VARCHAR(128) NOT NULL,
                              FirstName VARCHAR(26) NOT NULL,
                              Surname VARCHAR(26) NOT NULL,
                              ContactNo CHAR(11) NOT NULL
                              )''')

    def RegisterUser(self):
        query = """INSERT INTO UserTable (UserEmail, UserSalt, PasswordHash, FirstName, Surname, ContactNo) VALUES (?, ?, ?, ?, ?, ?)"""
        values = (self.Email, self.Salt, self.Password, self.Name, self.Surname, self.ContactNo)

        self.cursor.execute(query, values)
        self.connection.commit()

    def GetSalt(self, Email):
        query = """SELECT UserSalt FROM UserTable WHERE UserEmail = ?"""
        self.cursor.execute(query, (Email,))
        User_salt = self.cursor.fetchone()

        if len(User_salt) != 0:
            return User_salt[0]
        else:
            return None

    def VerifyEmail(self, UserEmail):
        query = """SELECT UserEmail FROM UserTable WHERE UserEmail = ?"""
        self.cursor.execute(query, (UserEmail,))
        User_Email = self.cursor.fetchone()  # Store the email address fetched from database

        # compare the Email address, if match: return True
        if (User_Email[0]) == UserEmail:
            return True
        else:
            return False

    def VerifyPassword(self, UserEmail, Password):
        query = """SELECT PasswordHash FROM UserTable WHERE UserEmail = ?"""
        self.cursor.execute(query, (UserEmail,))
        User_Hash = self.cursor.fetchone()  # Store the PasswordHash fetched from database

        # compare the Password Hash, if match: return True
        if (User_Hash[0]) == Password:
            return True
        else:
            return False
