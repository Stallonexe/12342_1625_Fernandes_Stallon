class Booking:
    def __init__(self, PropertyID, UserID):
        self.PropertyID = PropertyID
        self.UserID = UserID

        self.week = {'monday':[],
                     'tuesday':[],
                     'wednesday':[],
                     'thursday':[],
                     'friday':[],
                     'saturday':[],
                     'sunday':[]}
        self.START_TIME = 9
        self.MAX_APPOINTMENTS_PER_DAY = 10

        self.BookAppointments()

    def GetAppointments(self):
        print("\n############################################################\n")
        for Day in self.week:
            print(f"{Day}   : {self.MAX_APPOINTMENTS_PER_DAY - len(self.week[Day])} appointments left")
        print("\n############################################################\n")

        #Query database, remove timing from week that r not available

    def BookAppointments(self):
        self.GetAppointments()

        Day = input("Which day do you prefer ?  ").lower()
        Time = self.START_TIME + len(self.week[Day])
        print(f"Next Appointment on {Day} is at {Time} : 00")

        BookingChoice = input("\n\Type anything to cancel\nDo you want to book? [y/n]").lower()

        if BookingChoice == 'y':
            self.week[Day].append(self.UserID)
        elif BookingChoice == 'n':
            self.BookAppointments()
