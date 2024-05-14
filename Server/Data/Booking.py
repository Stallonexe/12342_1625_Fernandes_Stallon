import sqlite3

class Booking:
    def __init__(self):

        #Database
        self.connection = sqlite3.connect('Data/Database/Booking.db')
        self.cursor = self.connection.cursor()

        #Methods
        self.CreateBookingTable()

    def CreateBookingTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS BookingTable
                          (
                          DateTimeofAppointment DATETIME PRIMARY KEY NOT NULL,
                          UserEmail VARCHAR(320) NOT NULL,
                          AgentEmail VARCHAR(320) NOT NULL,
                          PropertyID VARCHAR(6) NOT NULL
                          )''')


    def BookAppointment(self, DateTimeofAppointment, UserEmail, AgentEmail, PropertyID ):
        query = """INSERT INTO BookingTable (DateTimeofAppointment, UserEmail, AgentEmail, PropertyID) VALUES (?, ?, ?, ?)"""
        values = (DateTimeofAppointment, UserEmail, AgentEmail, PropertyID)

        self.cursor.execute(query, values)
        
        try:
            self.connection.commit()
        except:
            return "unavailable"
            
#booking_assistant = Booking()

#DateTimeofAppointment = '2023-03-15 14:00:00'
#UserEmail = 'johndoe@example.com'
#AgentEmail = 'janedoe@example.com'
#PropertyID = '123456'

#booking_assistant.BookAppointment(DateTimeofAppointment, UserEmail, AgentEmail, PropertyID)