class Booking:
    def __init__(self, PropertyID):
        self.PropertyID = PropertyID

        self.week = {'Monday':[5,10,11,12,13,14,15],
                     'Tuesday':[11,12,13,15],
                     'Wednesday':[16,17,18,19],
                     'Thursday':[4],
                     'Friday':[18],
                     'Saturday':[15],
                     'Sunday':[14,16,18]}

        self.GetAppointments()

    def GetAppointments(self):
        print()
        #Query database, remove timing from week that r not available

    def FindAvailability(self, UserID):
        self.UserID = UserID


        for day in self.week:
            AvailableAppointments = len(self.week[day])

            if AvailableAppointments != 0:
                print(f"########## Booking Available ###########")
                print(f"{day}:  \n")

                for time in self.week[day]:
                    print(f"{time} : 00\n")
                print(f"########################################\n")

                Time = int(input("What time do you want to view the Property? [type 0 to show more]"))

                if Time != 0:
                    self.BookAppointment(day, Time)

            else:
                print("No Appointments Available !")
                return True

    def BookAppointment(self, Day, Time):
        return f"Book {self.UserID} {self.PropertyID} {Day} {Time}"
        #SQL book









