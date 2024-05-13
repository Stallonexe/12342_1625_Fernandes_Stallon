import sqlite3

class User:
    def __init__(self):

        #Database
        self.connection = sqlite3.connect('Data/Database/login.db')
        self.cursor = self.connection.cursor()

        #Methods
        self.CreateUserTable()

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

    def RegisterUser(self, UserEmail, UserSalt, Password, FirstName, Surname, ContactNo):
        query = """INSERT INTO UserTable (UserEmail, UserSalt, PasswordHash, FirstName, Surname, ContactNo) VALUES (?, ?, ?, ?, ?, ?)"""
        values = (UserEmail, UserSalt, Password, FirstName, Surname, ContactNo,)

        self.cursor.execute(query, values)
        self.connection.commit()

    def GetSalt(self, Email):
        query = """SELECT UserSalt FROM UserTable WHERE UserEmail = ?"""
        self.cursor.execute(query, (Email,))
        User_salt = self.cursor.fetchone()

        if User_salt is not None and len(User_salt) != 0:
            return User_salt[0]
        else:
            return None

    def GetName(self, Email):
        query = """SELECT FirstName FROM UserTable WHERE UserEmail = ?"""
        self.cursor.execute(query, (Email,))
        Name = self.cursor.fetchone()

        if Name is not None and len(Name) != 0:
            return Name[0]
        else:
            return None


    def VerifyEmail(self, UserEmail):
        query = """SELECT UserEmail FROM UserTable WHERE UserEmail = ?"""
        self.cursor.execute(query, (UserEmail,))
        User_Email = self.cursor.fetchone()  # Store the email address fetched from database

        # compare the Email address, if match: return True
        if User_Email is not None and (User_Email[0]) == UserEmail:
            return True
        else:
            return False

    def VerifyPassword(self, UserEmail, Password):
        query = """SELECT PasswordHash FROM UserTable WHERE UserEmail = ?"""
        self.cursor.execute(query, (UserEmail,))
        User_Hash = self.cursor.fetchone()  # Store the PasswordHash fetched from database

        # compare the Password Hash, if match: return True
        if User_Hash is not None and (User_Hash[0]) == Password:
            return True
        else:
            return False

class Agent(User):
    def __init__(self):
        super(Agent, self).__init__()


    def CreateAgentTable(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS AgentTable
                              (
                              AgentEmail VARCHAR(320) PRIMARY KEY NOT NULL,
                              AgencyName VARCHAR(320) NOT NULL,
                              FOREIGN KEY (AgentID) REFERENCES UserTable (UserEmail),
                              FOREIGN KEY (PropertyID) REFERENCES PropertyTable (PropertyID)
                              )''')
