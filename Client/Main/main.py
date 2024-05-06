import time
from Functions import *
from Booking import *



class Screen:
    def __init__(self):
        self.logo = """
██╗░░██╗  ░█████╗░  ██╗░░░██╗  ░██████╗  ██╗  ███████╗  ██╗░░░██╗
██║░░██║  ██╔══██╗  ██║░░░██║  ██╔════╝  ██║  ██╔════╝  ╚██╗░██╔╝
███████║  ██║░░██║  ██║░░░██║  ╚█████╗░  ██║  █████╗░░  ░╚████╔╝░
██╔══██║  ██║░░██║  ██║░░░██║  ░╚═══██╗  ██║  ██╔══╝░░  ░░╚██╔╝░░
██║░░██║  ╚█████╔╝  ╚██████╔╝  ██████╔╝  ██║  ██║░░░░░  ░░░██║░░░ Program
╚═╝░░╚═╝  ░╚════╝░  ░╚═════╝░  ╚═════╝░  ╚═╝  ╚═╝░░░░░  ░░░╚═╝░░░ Made By Stallon"""

        #Constants
        self.INF = 1000000

        self.Preference = {}
        self.Salt = gen_salt()

        #main
        self.LikedProperties = []

        self.SeenList = []
        self.SeenDict = {}



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

                    MatchedPassword = HashPassword(self.Salt, Password)

                    if MatchedPassword == True:
                        print("\nLogin Successful !")
                        self.PreferenceScreen()
                        break

                    else:
                        print(f"\nIncorrect Password!\nYou have {3 - ATTEMPTS} attempts Left!")
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

        try:
            ContactNo = int(input("Phone Number    :     "))
        except:
            print("[*] Please input a valid phone number !!!\n")
            try:
                ContactNo = int(input("Phone Number    :     "))
            except:
                ContactNo = 0

        print()
        UserEmail, Password, RepeatPassword = LoginInput()

        while Password != RepeatPassword and len(Password) < 6:
            print("\n   *** Both Passwords Don't Match or is less than 6 characters ***\n")
            UserEmail, Password, RepeatPassword = LoginInput()

        HashedPassword = HashPassword(self.Salt, Password)
        #REGISTER WITH SERVER
        print("\nRegistration Successful !\nPlease Login\n")
        self.LoginScreen(EnableOTP=True)



    def PreferenceScreen(self):
        time.sleep(1)
        print("\n##########################################################################################\n")
        print("#                                    USER PREFERENCES                                    #")
        print("\n##########################################################################################\n")
        location = str(input("Location       :     ")).lower()
        postcode = PostCode(location)
        print(postcode)
        print("\n[Detached][Semidetached][Terraced][Apartment][Flat][Bungalow]")
        propertytype = str(input("Property Type  :     ")).lower()

        try:
            max_price = int(input("Max House Price:     "))
            min_price = int(input("Min House Price:     "))

            BedroomNo = int(input("Bedrooms       :     "))
            BathroomNo = int(input("Bathrooms      :     "))
            LivingroomNo = int(input("Living rooms   :     "))
        except:
            max_price = self.INF
            min_price = self.INF
            BedroomNo = self.INF
            BathroomNo = self.INF
            LivingroomNo = self.INF

        print("\n##########################################################################################\n")
        # GetProperty from server # get graph

        self.Property = readJson('Property.json')
        self.PropertyList = GetPropertyList(self.Property)

        print("Based on your preferences, here are some properties that you may like.")
        self.SearchProperties()
        print("\n##########################################################################################\n")
        #Get Property###############

    def SearchProperties(self):
        SAMPLE_SIZE = 3
        Sample = SimpleRandomSample(self.PropertyList, SAMPLE_SIZE)

        for i in range(0,3):
            ID = Sample[i]
            self.DisplayProperty(ID)

        root = self.SeenList[0]

        graph = Graph(self.Property)
        matrix = Matrix()
        matrix.AppendMatrix(graph.getmatrix())

        Rank = matrix.GetRank()
        for ID in Rank:
            if ID not in self.SeenList:
                self.DisplayProperty(ID)


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
        self.LikedProperties.append(PropertyID)
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
        if PropertyID in self.LikedProperties:
            TimeDuration += 10 # acts as a bias

        self.SeenList.append(str(PropertyID))
        self.SeenDict[str(PropertyID)] = int(TimeDuration)

        self.RankList()

    def DisplayBooking(self):
        print("\n##########################################################################################\n")

    def RankList(self):
        self.SeenList = sorted(self.SeenList, key=lambda ID: self.SeenDict[ID], reverse=True)







Main = Screen()

Main.StartScreen()