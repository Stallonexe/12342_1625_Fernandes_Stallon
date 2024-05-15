class Booking:
    def __init__(self, PropertyID, UserID):
        self.PropertyID = PropertyID
        self.UserID = UserID

        self.week = {'monday': [],
                     'tuesday': [],
                     'wednesday': [],
                     'thursday': [],
                     'friday': [],
                     'saturday': [],
                     'sunday': []}
        self.START_TIME = 9
        self.MAX_APPOINTMENTS_PER_DAY = 10


    def GetAppointments(self):
        print("\n############################################################\n")

        for Day in self.week:
            print(f"{Day.upper()}   : {self.MAX_APPOINTMENTS_PER_DAY - len(self.week[Day])} appointments left")

        print("\n############################################################\n")


    def BookAppointments(self):

        self.GetAppointments()

        while True:
            Day = input("Which day do you prefer ?  ").lower()

            if Day in self.week.keys():
                if len(self.week[Day]) < self.MAX_APPOINTMENTS_PER_DAY:
                    self.Time = self.START_TIME + len(self.week[Day])
                    break
                else:
                    print("No available slots on this day. Please choose another day.")
            else:
                print("Type a valid day!\n")

        print(f"Next Appointment on {Day} is at {self.Time} : 00")

        BookingChoice = input("\nType anything to cancel\nDo you want to book? [y/n]").lower()

        self.BookingData = []

        if BookingChoice == 'y':
            self.week[Day].append(self.UserID)
            self.BookingData.append(Day)
            self.BookingData.append(self.Time)

            print("\nA booking confirmation email has been sent. Please check your inbox.\n")
            return self.BookingData

        elif BookingChoice == 'n':
            print("Booking cancelled.")
            return []

        else:
            print("Invalid choice, booking process is cancelled.")
            return []
