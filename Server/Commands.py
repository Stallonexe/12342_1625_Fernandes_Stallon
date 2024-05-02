from Data.Users import User
from Data.Property import Property

from Login_System.Server_Login_System import *
from Email_System.Email_Sender import *


def execute(message, cursor, connection):
    command = message.split()

    if command[0] == "Create":
        if command[1] == "RegUser":
            User(command[2], command[3], command[4], command[5], command[6], command[7])

        elif command[1] == "RegProperty":
            Property(command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9], command[10], command[11], command[12])
        else:
            return "INVALID"

    elif command[0] == "Retrieve":
        if command[1] == "Salt":
            User_salt = User.GetSalt(command[2], cursor, connection)

            if len(User_salt) != 0:
                return User_salt[0]
            else:
                return None

        elif command[1] == "PropertyJSON":
            pass
        else:
            return "INVALID"

    elif command[0] == "Update":
        if command[1] == "Salt":
            pass
        elif command[1] == "PropertyJSON":
            pass
        else:
            return "INVALID"

    elif command[0] == "Delete":
        if command[1] == "Salt":
            pass
        elif command[1] == "PropertyJSON":
            pass
        else:
            return "INVALID"

    elif command[0] == "Verify":
        if command[1] == "Salt":
            pass
        elif command[1] == "PropertyJSON":
            pass
        else:
            return "INVALID"

    elif command[0] == "Send":
        if command[1] == "Salt":
            pass
        elif command[1] == "PropertyJSON":
            pass
        else:
            return "INVALID"

    elif command[0] == "Generate":
        if command[1] == "Salt":
            pass
        elif command[1] == "PropertyJSON":
            pass
        else:
            return "INVALID"
    else:
        return "INVALID"


execute("Create RegUser dorisanta@il. ABCDEF Password FirstName Surname 07440423797", "", "")
execute("Create RegProperty ASDFGH 450000 77CoplandRoad HA04YF 1 1 1 Freehold C Flat C","","")
cursor.close()
connection.close()