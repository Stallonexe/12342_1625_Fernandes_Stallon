from Login_System.Server_Login_System import *
from Email_System.Email_Sender import *
#email


def dexecute(message, cursor, connection):
    command = message.split()

    if command[0] == "!Register":
        register(command[1], command[2], command[3], command[4], command[5], command[6], cursor, connection)
        return ""

    elif command[0] == "!Get":
        if command[1] == "Salt":
            User_salt = get_salt(command[2], cursor, connection)

            if len(User_salt) != 0:
                return User_salt[0]
            else:
                return None

    elif command[0] == "!Verify":
        if command[1] == "Email":
            UserEmail = verify_email(command[2], cursor, connection)

            if UserEmail:
                return "True"
                print("True")
            else:
                return "False"

        elif command[1] == "Hash":
            UserHash = verify_hash(command[2], command[3], cursor, connection)

            if UserHash:
                return "True"
            else:
                return "False"

    elif command[0] == "!Send":
        if command[1] == "OTP":
            email.SendOTP(command[2],command[3])
        elif command[1] == "BookingConfirmation":
            email.SendBookingConfirmation(command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9])


    else:
        return "INVALID"


def execute(message, cursor, connection):
    command = message.split()

    if command[0] == "Create":
        if command[1] == "RegUser":
            register(command[2], command[3], command[4], command[5], command[6], command[7], cursor, connection)

        elif command[1] == "RegProperty":
            pass
        else:
            return "INVALID"

    elif command[0] == "Retrieve":
        if command[1] == "Salt":
            User_salt = get_salt(command[2], cursor, connection)

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

cursor.close()
connection.close()