import time
from Client.Functions import *
from Client.Modules.Email_Sender import email
#from Client.Modules.Client import *
from Client.Modules.Booking import *



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
            self.UserEmail = input("Enter Email :     ")
            self.Name = input("Enter Name  :     ")
            self.UserID = "U1"
            VerifyEmail = True # server


            if VerifyEmail == True:
                ATTEMPTS = 0

                try:
                    SentOTP = email.SendOTP(self.UserEmail, self.Name)
                    #print(SentOTP)
                except:
                    print("Invalid details inputted ! \nPlease Try Again !")
                    self.LoginScreen(EnableOTP=True)
                while ATTEMPTS != 3:

                    ATTEMPTS += 1
                    #send otp


                    print(f"\nAn OTP-Code has been sent to {self.UserEmail}\n Type 0 to try again\n")
                    print()
                    InputOTP = int(input("OTP         :     "))


                    if InputOTP == 0:
                        self.LoginScreen(EnableOTP=True)

                    elif int(InputOTP) == SentOTP:
                        print("\nLogin Successful !")
                        self.PreferenceScreen()
                        break


                    else:
                        print(f"\nInvalid OTP!\nYou have {ATTEMPTS - 3} attempts Left!")
                        print("\n##########################################################################################\n")
                time.sleep(3)
                self.LoginScreen(EnableOTP=False)
            else:
                print(f"{self.UserEmail} is not Registered !")
                time.sleep(2)
                self.StartMenu()
        else:
            print()
            self.UserEmail = input("Enter Email :     ")

            Send(f"!Verify Email {self.UserEmail}")
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
                        print(f"\nIncorrect Password!\nYou have {-1*(3 - ATTEMPTS)} attempts Left!")
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
        self.UserEmail, Password, RepeatPassword = LoginInput()

        while Password != RepeatPassword and len(Password) < 6:
            print("\n   *** Both Passwords Don't Match or is less than 6 characters ***\n")
            self.UserEmail, Password, RepeatPassword = LoginInput()

        HashedPassword = HashPassword(self.Salt, Password)

        server_command = f"!Register {self.UserEmail} {self.Salt} {HashedPassword} {UserName} {Surname} {ContactNo}"
        #Send(server_command)

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

        self.Property = ''
        while len(self.Property) == 0:
            self.Property = readJson('Property.json')

        self.PropertyList = GetPropertyList(self.Property)

        print("Based on your preferences, here are some properties that you may like.")
        self.SearchProperties()
        print("\n##########################################################################################\n")
        #Get Property###############

    def SearchProperties(self):
        SAMPLE_SIZE = 3
        Sample = SimpleRandomSample(self.PropertyList, SAMPLE_SIZE)

        for i in range(0, 3):
            ID = Sample[i]
            self.DisplayProperty(ID)

        Root1 = self.SeenList[0]
        Root2 = self.SeenList[1]
        Root3 = self.SeenList[2]

        # Change Start
        graph1 = Graph(Root_node=Root1, Samplelist=Sample, PropertyDict=self.Property)
        graph2 = Graph(Root_node=Root2, Samplelist=Sample, PropertyDict=self.Property)
        graph3 = Graph(Root_node=Root3, Samplelist=Sample, PropertyDict=self.Property)

        matrix = Matrix()

        matrix.AppendMatrix(graph1.getmatrix())
        Rank1 = matrix.GetRank()

        matrix.AppendMatrix(graph2.getmatrix())
        Rank2 = matrix.GetRank()

        matrix.AppendMatrix(graph3.getmatrix())
        Rank3 = matrix.GetRank()

        Rank1 = RomoveRoot(Root1, Rank1)
        Rank2 = RomoveRoot(Root2, Rank2)
        Rank3 = RomoveRoot(Root3, Rank3)

        FinalRank = CompareRanking(Rank1, Rank2, Rank3)

        for ID in FinalRank:
            self.DisplayProperty(ID)

        print("\n##########################################################################################\n")
        print("#                                       END OF PAGE                                       #")
        print("\n##########################################################################################\n")
        print("\nPlease update your preferences, to  search for more properties.\n")

        self.PreferenceScreen()

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
                booking = Booking(PropertyID,self.UserID)
                bookingdata = booking.BookAppointments()

                if len(bookingdata) != 0:
                    Day = bookingdata[0]
                    AppointmentTime = bookingdata[1]
                    Address = self.Property[PropertyID]["address"]
                    postcode = self.Property[PropertyID]["PostCode"]

                    email.SendBookingConfirmation(self.UserEmail, self.Name, 'St Gregorys Estate', 'Stallon', Day, AppointmentTime, Address, postcode)


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