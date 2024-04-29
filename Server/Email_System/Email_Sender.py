import os
import ssl
from email.message import EmailMessage
import smtplib
import random




class Email:
    def __init__(self):
        self.sender = 'developer.housify@gmail.com'
        self.password = 'uitmwwltbusdegza'

    def GenOTP(self):
        OTP_array = []
        for i in range(6):
            number = random.randrange(0, 9, 1)
            OTP_array.append(number)
        OTP_String = int(''.join(map(str, OTP_array)))
        print(OTP_String)
        return OTP_String

    def SendOTP(self, recipient_email, recipient_name):
        Subject = 'Verify your Housify account'
        OTP = self.GenOTP()

        Body = f"""
        Dear {recipient_name},

        Thank you for using Housify!

        H - {OTP} is your Housify verification code.

        Best regards,
        
        Housify Team
                """

        Email = EmailMessage()

        Email['From'] = self.sender
        Email['To'] = recipient_email
        Email['Subject'] = Subject
        Email.set_content(Body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, recipient_email, Email.as_string())

    def SendBookingConfirmation(self, recipient_email, recipient_name, AgencyName, Agent, BookingDate, BookingTime, Address, PostCode):
        Subject = 'Your viewing request has been approved.'

        Body = f"""
        Dear {recipient_name},

        Your viewing request has been approved.
        
        Address:    {Address} {PostCode}
        Date:       {BookingDate}
        Time:       {BookingTime}
        
        Your appointment will be with:

        {Agent}, from {AgencyName}.
        
        Please arrive 10 min before your appointment.

        Best regards,

        Housify Team
                """

        Email = EmailMessage()

        Email['From'] = self.sender
        Email['To'] = recipient_email
        Email['Subject'] = Subject
        Email.set_content(Body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, recipient_email, Email.as_string())


email = Email()

#email.SendOTP('developer.housify@gmail.com', 'Stallon')
#email.SendBookingConfirmation('ferns311@stgregorys.school','Stallon')
#email.SendBookingConfirmation('ferns311@stgregorys.school', 'Stallon','St Gregorys Estate','Denzil','11/05/2024','15:00','3 Potters Road Southall', 'UB2 4AS')



