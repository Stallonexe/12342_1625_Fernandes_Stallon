import sqlite3

from Data.Users import *
from Data.Property import *
#from Modules.functions import writeJson

#from Email_System.Email_Sender import *
#from Server.Server_Login_System import *


class Command:
    def __init__(self):
        self.LoginFILEPATH = "Server\Files\login.db"
        self.PropertyFILEPATH = "Server\Files\Property.db"
        self.BookingFILEPATH = "Server\Files\Booking.db"  # No such file yet

        self.User = User()
        self.house = PropertySQL()
       # self.house = House()

    def ConnectLoginDatabase(self):
        self.connection = sqlite3.connect(self.LoginFILEPATH)
        self.cursor = self.connection.cursor()

    def ConnectPropertyDatabase(self):
        self.connection = sqlite3.connect(self.PropertyFILEPATH)
        self.cursor = self.connection.cursor()

    def ConnectBookingDatabase(self):
        self.connection = sqlite3.connect(self.BookingFILEPATH)
        self.cursor = self.connection.cursor()

    def execute(self, message):
        command = message.split()
        print(command)

        if command[0] == "Create":

            if command[1] == "RegUser":
                #self.ConnectLoginDatabase()
                self.User.RegisterUser(command[2], command[3], command[4], command[5], command[6], command[7])
                return ""

            elif command[1] == "RegProperty":
                #self.ConnectPropertyDatabase()
                self.house.AddProperty(command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9], command[10], command[11], command[12])
                return ""

            elif command[1] == "Booking":
                self.ConnectBookingDatabase()
                # make booking table + commands to qeury

            else:
                return ""

        elif command[0] == "Retrieve":

            if command[1] == "Salt":

                #self.ConnectLoginDatabase()
                salt = self.User.GetSalt(command[2])
                return salt

            elif command[1] == "Name":

                #self.ConnectLoginDatabase()
                Name = self.User.GetName(command[2])
                return Name


        elif command[0] == "Delete":

            if command[1] == "User":
                return None  # for future features

            elif command[1] == "Property":
                return None  # for future features

        elif command[0] == "Verify":

            if command[1] == "Email":
                verify = self.User.VerifyEmail(command[2])
                if verify:
                    return "True"
                else:
                    return "False"

            if command[1] == "Password":
                verify = self.User.VerifyPassword(command[2], command[3])
                if verify:
                    return "True"
                else:
                    return "False"

        elif command[0] == "Send":

            if command[1] == "PropertyJSON":
                saved = self.house.GetProperty(command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9], command[10])

                if saved:
                    return "True"
                else:
                    return "False"


#decoder = Command()
#decoder.execute("Create RegUser stallonfernandes11@gmail.com ABCDEF Password FirstName Surname 07440423797")
#print(decoder.execute("Retrieve Salt stallonfernandes11@gmail.com"))
#print(decoder.execute("Verify Email stallonfernandes11@gmail.com"))
#print(decoder.execute("Verify Password stallonfernandes11@gmail.com  Password"))
#print(decoder.execute("Verify Email stallonfernandes11@gmail.com"))

#decoder.execute("Create RegProperty H10 350000 77CoplandRoad HA04YF 1 1 1 leasehold C FLAT B")
#print(decoder.execute("Send PropertyJSON U2 400000 100000 HA 1 1 1 leasehold FLAT"))
#print(decoder.execute("Verify Email stallonfernandes11@gmail.com"))
#print(decoder.execute("Verify Email stallonfernandes11@gmail.com"))







# execute("Create RegUser dorisanta@il. ABCDEF Password FirstName Surname 07440423797", "", "")
# execute("Create RegProperty ASDFGH 450000 77CoplandRoad HA04YF 1 1 1 Freehold C Flat C","","")
# cursor.close()
# connection.close()