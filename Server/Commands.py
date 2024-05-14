from Data.Users import *
from Data.Property import *
from Data.Booking import *


class Command:
    def __init__(self):
        self.User = User()
        self.agent = Agent()
        self.house = PropertySQL()
        self.booking = Booking()


    def execute(self, message):
        command = message.split()
        print(command)

        if command[0] == "Create":

            if command[1] == "RegUser":
                if command[8] != "null":
                    self.agent.RegisterAgent(command[2], command[8])
                else:
                    self.User.RegisterUser(command[2], command[3], command[4], command[5], command[6], command[7])
                

                return ""


            elif command[1] == "RegProperty":
                self.house.AddProperty(command[2], command[3], command[4], command[5], command[6], command[7], 
                command[8], command[9], command[10], command[11], command[12])
                return ""

            elif command[1] == "Booking":
                reply = self.booking.BookAppointment(command[2], command[3], command[4], command[5])
                return reply
                
            else:
                return ""

        elif command[0] == "Retrieve":
            if command[1] == "Salt":
                salt = self.User.GetSalt(command[2])
                return salt

            elif command[1] == "Name":

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

                max_price = int(command[2])
                min_price = int(command[3])
                postcode = str(command[4])
                bedroom = int(command[5])
                bathroom = int(command[6])
                living_room = int(command[7])
                tenure = str(command[8])
                property_type = str(command[9])



                PropertyDict = self.house.GetProperty(max_price, min_price, postcode, bedroom, bathroom,
                 living_room, tenure, property_type)

                if len(PropertyDict) != 0:
                    return PropertyDict
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