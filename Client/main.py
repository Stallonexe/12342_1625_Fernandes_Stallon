import time
from Functions import *
from Modules.Email_Sender import email
from Modules.Booking import *
from Modules.Client import *



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
            VerifyEmail = Send(f"Verify Email {self.UserEmail}") # change

            self.Name = Send(f"Retrieve Name {self.UserEmail}")  # change

            #print(f"Verify {VerifyEmail}")
            #print(f"Name{self.Name}")
            if VerifyEmail == "True": #change
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

            VerifyEmail = Send(f"Verify Email {self.UserEmail}")


            if VerifyEmail == "True":
                ATTEMPTS = 0
                while ATTEMPTS != 3:

                    ATTEMPTS += 1

                    Password = input("Password    :     ")

                    self.Salt = Send(f"Retrieve Salt {self.UserEmail}") # change
                    HashedPassword = HashPassword(self.Salt, Password) # change

                    MatchedPassword = Send(f"Verify Password {self.UserEmail} {HashedPassword}") #change

                    if MatchedPassword == "True":
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

        #Start Change
        print()
        agent = input("Are you a real estate agent?  [y/n]").lower()

        if agent == "y":
            agency = input("What agency do you work for ?")
        else:
            agency = "null"

        server_command = f"Create RegUser {self.UserEmail} {self.Salt} {HashedPassword} {UserName} {Surname} {ContactNo} {agency}"
        reply = Send(server_command)

        if reply == "Done":
            print("\nRegistration Successful !\nPlease Login\n")
            self.LoginScreen(EnableOTP=True)
        else:
            print("\nRegistration failed !! [Returning to Start Menu ... ]\n")
            self.StartMenu()

        #End change




    def PreferenceScreen(self):
        time.sleep(1)
        print("\n##########################################################################################\n")
        print("#                                    USER PREFERENCES                                    #")
        print("\n##########################################################################################\n")
        location = str(input("Location       :     ")).upper() # change
        postcode = PostCode(location)
        #print(postcode)
        print("\n[Detached][Semidetached][Terraced][Apartment][Flat][Bungalow]")
        propertytype = str(input("Property Type  :     ")).upper() # change
        print("\nTenure Options: Leasehold Or Freehold") #change
        tenure = str(input("Tenure:     ")).upper() # change

        try:
            max_price = int(input("Max House Price:     "))
            min_price = int(input("Min House Price:     "))

            BedroomNo = int(input("Bedrooms       :     "))
            BathroomNo = int(input("Bathrooms      :     "))
            LivingroomNo = int(input("Living rooms   :     "))
        except:
            max_price = self.INF
            min_price = 0 #change here
            BedroomNo = self.INF
            BathroomNo = self.INF
            LivingroomNo = self.INF

        print("\n##########################################################################################\n")
        # GetProperty from server # get graph

        #change
        self.Property = Send(f"Send PropertyJSON {max_price} {min_price} {postcode} {BedroomNo} {BathroomNo} {LivingroomNo} {tenure} {propertytype}")

        while len(self.Property) == 0 or self.Property == "False": # change
            self.Property = readJson('Property.json')

        self.PropertyList = GetPropertyList(self.Property)
        print(self.Property)
        print()
        print(self.PropertyList)

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

        logout = input("Do you want to log out ? [y/n]").lower()

        if logout == "y":
            Send(DISCONNECT_MESSAGE)
            exit()
        else:
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
                
                - Ad by {self.Property[PropertyID]["Agency"]}
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
                booking = Booking(PropertyID,self.UserEmail) #change here
                bookingdata = booking.BookAppointments()

                if len(bookingdata) != 0 and bookingdata is not None:
                    Day = str(bookingdata[0])
                    AppointmentTime = bookingdata[1]
                    Address = self.Property[PropertyID]["address"]
                    postcode = self.Property[PropertyID]["PostCode"]
                    Agency = self.Property[PropertyID]["Agency"]
                    DateTimeofAppointment = GetDateTime(Day, AppointmentTime)

                    AgentEmail = Send(f"Retrieve AgentEmail {Agency}") # can fix this by random
                    AgentName = Send(f"Retrieve Name {AgentEmail}")  # change



                    reply = Send(f"Create Booking {DateTimeofAppointment} {self.UserEmail} {AgentEmail} {PropertyID}")  # commands[i] fix this
                    if reply == "unavailable":
                        print(f"\nThe appointment you selected is unavailable, please contact {Agency}! \n")
                    else:
                        email.SendBookingConfirmation(self.UserEmail, self.Name, Agency, AgentName, DateTimeofAppointment, Address, postcode)


        TimeDuration = End_time - Start_time
        if PropertyID in self.LikedProperties:
            TimeDuration += 10 # acts as a bias

        self.SeenList.append(str(PropertyID))
        self.SeenDict[str(PropertyID)] = int(TimeDuration)

        self.RankList()

    def RankList(self):
        self.SeenList = sorted(self.SeenList, key=lambda ID: self.SeenDict[ID], reverse=True)







Main = Screen()

Main.StartScreen()