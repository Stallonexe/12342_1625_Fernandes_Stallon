from Data.Users import User
from Data.Property import Property


from Email_System.Email_Sender import *
from Server.Server_Login_System import *


class Command:
    def __init__(self):
        self.LoginFILEPATH = "Server\Files\login.db"
        self.PropertyFILEPATH = "Server\Files\Property.db"
        self.BookingFILEPATH = "Server\Files\Booking.db"  # No such file yet

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

        if command[0] == "Create":

            if command[1] == "RegUser":
                self.ConnectLoginDatabase()
                register(command[2], command[3], command[4], command[5], command[6], command[7], self.cursor)

            elif command[1] == "RegProperty":
                self.ConnectPropertyDatabase()
                # make property commands + sql

            elif command[1] == "Booking":
                self.ConnectBookingDatabase()
                # make booking table + commands to qeury

            else:
                return ""

        elif command[0] == "Retrieve":

            if command[1] == "Salt":

                self.ConnectLoginDatabase()
                salt = get_salt(command[2], self.cursor)
                return salt

            elif command[1] == "Name":

                self.ConnectLoginDatabase()
                Name = get_name(command[2], self.cursor)

            elif command[1] == "PropertyList":
                self.ConnectPropertyDatabase()


        elif command[0] == "Delete":

            if command[1] == "User":
                return None  # for future features

            elif command[1] == "Property":
                return None  # for future features

        elif command[0] == "Verify":
            self.ConnectLoginDatabase()

            if command[1] == "Email":
                verify = verify_email(command[2], self.cursor)
                return verify

            if command[1] == "Password":
                verify = verify_hash(command[2], command[3], self.cursor)
                return verify

        elif command[0] == "Send":

            if command[1] == "PropertyJSON":
                self.ConnectPropertyDatabase()
                Property = {}  # create a subroutine that qeury property.db, that will return dict contain property info
                # takes list of propertyIDs as parameter


com = Command()
com.execute("Create RegUser stallonfernandes11@gmail.com ABCDEF Password FirstName Surname 07440423797")

# execute("Create RegUser dorisanta@il. ABCDEF Password FirstName Surname 07440423797", "", "")
# execute("Create RegProperty ASDFGH 450000 77CoplandRoad HA04YF 1 1 1 Freehold C Flat C","","")
# cursor.close()
# connection.close()