import random
import time
import hashlib


def HashPassword(UserEmail, Password):
    #Get Salt
    UserSalt = "ABCDE"
    Password += UserSalt
    PasswordBytes = Password.encode('utf-8')

    SHA256 = hashlib.sha256()
    SHA256.update(PasswordBytes)
    HashedPassword = SHA256.hexdigest()

    return HashedPassword

def GetPropertyList():
    PropertyList = []
    for house in Property:
        PropertyList.append(house)
    return PropertyList

class Screen:
    def __init__(self,  PropertyList, Property):
        self.logo = """
██╗░░██╗  ░█████╗░  ██╗░░░██╗  ░██████╗  ██╗  ███████╗  ██╗░░░██╗
██║░░██║  ██╔══██╗  ██║░░░██║  ██╔════╝  ██║  ██╔════╝  ╚██╗░██╔╝
███████║  ██║░░██║  ██║░░░██║  ╚█████╗░  ██║  █████╗░░  ░╚████╔╝░
██╔══██║  ██║░░██║  ██║░░░██║  ░╚═══██╗  ██║  ██╔══╝░░  ░░╚██╔╝░░
██║░░██║  ╚█████╔╝  ╚██████╔╝  ██████╔╝  ██║  ██║░░░░░  ░░░██║░░░ Program
╚═╝░░╚═╝  ░╚════╝░  ░╚═════╝░  ╚═════╝░  ╚═╝  ╚═╝░░░░░  ░░░╚═╝░░░ Made By Stallon"""

        self.Preference = {}

        #main
        self.PropertyList = PropertyList
        self.LikedProperties = []

        self.SeenList = []
        self.SeenDict = {}

        self.Property = Property


    def StartScreen(self):
        print("##########################################################################################")
        print(self.logo)
        print()
        print("##########################################################################################\n")
        self.StartMenu()

    def StartMenu(self):
        UserReply = input("Do you have an account?  [y/n]       ").lower()
        print()
        if UserReply == "y":
            self.LoginScreen(EnableOTP=True)

        else:
            self.RegisterScreen()


    def LoginScreen(self, EnableOTP):
        time.sleep(2)
        print("\n##########################################################################################\n")
        print("#                                   LOGIN INTO HOUSIFY                                    #")
        print("\n##########################################################################################\n")

        if EnableOTP == True:
            UserEmail = input("Enter Email :     ")
            VerifyEmail = True # server

            if VerifyEmail == True:
                ATTEMPTS = 0
                while ATTEMPTS != 3:

                    ATTEMPTS += 1
                    #send otp
                    SentOTP = "ABCDEF"

                    print(f"\nAn OTP-Code has been sent to {UserEmail}\n")
                    InputOTP = input("OTP         :     ")

                    if InputOTP == SentOTP:
                        print("\nLogin Successful !")
                        self.PreferenceScreen()
                        break

                    else:
                        print(f"\nInvalid OTP!\nYou have {ATTEMPTS - 3} attempts Left!")
                        print("\n##########################################################################################\n")
                time.sleep(3)
                self.LoginScreen(EnableOTP=False)
            else:
                print(f"{UserEmail} is not Registered !")
                time.sleep(2)
                self.StartMenu()
        else:
            print()
            UserEmail = input("Enter Email :     ")
            VerifyEmail = True  # server

            if VerifyEmail == True:
                ATTEMPTS = 0
                while ATTEMPTS != 3:

                    ATTEMPTS += 1

                    Password = input("Password    :     ")

                    MatchedPassword = HashPassword(UserEmail, Password)

                    if MatchedPassword == True:
                        print("\nLogin Successful !")
                        self.PreferenceScreen()
                        break

                    else:
                        print(f"\nIncorrect Password!\nYou have {ATTEMPTS - 3} attempts Left!")
                        print("\n##########################################################################################\n")
                print("Please Try Again Later !")
                time.sleep(3)
                self.StartMenu()


    def RegisterScreen(self):
        def LoginInput():
            UserEmail = str(input("Email           :     "))
            Password = str(input("Password        :     "))
            RepeatPassword = str(input("Repeat Password :     "))
            return UserEmail, Password, RepeatPassword

        time.sleep(2)
        print("\n##########################################################################################\n")
        print("#                                   WELCOME TO HOUSIFY                                    #")
        print("\n##########################################################################################\n")

        print("\nIf you wish to return to Starting Menu, Type back. \n")

        UserName = str(input("Name            :     "))
        if UserName == "back":
            self.StartMenu()

        Surname = str(input("Surname         :     "))

        ContactNo = int(input("Phone Number    :     "))

        print()
        UserEmail, Password, RepeatPassword = LoginInput()

        while Password != RepeatPassword and len(Password) > 6:
            print("\n   *** Both Passwords Don't Match or is less than 6 characters ***\n")
            UserEmail, Password, RepeatPassword = LoginInput()

        #REGISTER WITH SERVER
        print("\nRegistration Successful !\nPlease Login\n")
        self.LoginScreen(EnableOTP=True)



    def PreferenceScreen(self):
        time.sleep(1)
        print("\n##########################################################################################\n")
        print("#                                    USER PREFERENCES                                    #")
        print("\n##########################################################################################\n")
        location = str(input("Location       :     ")).lower()
        propertytype = str(input("Property Type  :     ")).lower()

        max_price = int(input("Max House Price:     "))
        min_price = int(input("Min House Price:     "))

        BedroomNo = int(input("Bedrooms       :     "))
        BathroomNo = int(input("Bathrooms      :     "))
        LivingroomNo = int(input("Living rooms   :     "))
        print("\n##########################################################################################\n")

    def DisplayProperty(self, PropertyID):
        Text = f"""Property ID {PropertyID}.

                Property Info:
                - Address: {self.Property[PropertyID]["address"]}
                - PostCode: {self.Property[PropertyID]["PostCode"]}
                - Price: {self.Property[PropertyID]["Price"]}
                - Bedrooms: {self.Property[PropertyID]["Bedroom"]}
                - Bathrooms: {self.Property[PropertyID]["Bathroom"]}
                - Living rooms: {self.Property[PropertyID]["living_rooms"]}
                - Tenure:   {self.Property[PropertyID]["tenure"]}
                - Tax Band: {self.Property[PropertyID]["tax_band"]}
                - Property Type: {self.Property[PropertyID]["property_type"]}
                - EPC Rating: {self.Property[PropertyID]["EPC_rating"]}
                """

        Start_time = time.time()
        print("\n##########################################################################################\n")
        print(Text)
        print("\n##########################################################################################\n")

        UserOpinion = input("Do you like the property?  [y/n] ").lower()
        End_time = time.time()

        if UserOpinion == "y":
            self.LikedProperties.append(PropertyID)
            RequestBooking = input("Do you want to book a viewing? [y/n]").lower()

            if RequestBooking == "y":
                booking = Booking(PropertyID)
                while not True:
                    booking.FindAvailability(UserID)

                # Booking procedure

        TimeDuration = End_time - Start_time
        self.SeenList.append(str(PropertyID))
        self.SeenDict[str(PropertyID)] = int(TimeDuration)

        self.RankList()

    def DisplayBooking(self):
        print("\n##########################################################################################\n")

    def RankList(self):
        self.SeenList = sorted(self.SeenList, key=lambda ID: self.SeenDict[ID], reverse=True)







Main = Screen()

Main.StartScreen()