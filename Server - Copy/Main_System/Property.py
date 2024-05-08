import sqlite3
import random


connection = sqlite3.connect('Property.db')
cursor = connection.cursor()

def GenPropertyID():
    ID = []
    for i in range(6):
        ID.append(random.randrange(0,9))
    PropertyID = ''.join(ID)
    return PropertyID



# Create a UserTable
def CreatePropertyTable():

    cursor.execute('''CREATE TABLE IF NOT EXISTS PropertyTable
                  (
                  PropertyID CHAR(6) PRIMARY KEY NOT NULL,
                  PostCode CHAR(6) NOT NULL,
                  Price INTEGER NOT NULL,
                  Bedroom INTEGER NOT NULL,
                  Bathroom INTEGER NOT NULL,
                  Living_room INTEGER NOT NULL,
                  Tenure VARCHAR(2) NOT NULL,
                  Address VARCHAR(200) NOT NULL,
                  Tax_Band CHAR(1) NOT NULL,
                  Property_Type CHAR(2) NOT NULL,
                  EPC_rating CHAR(1)
                  )''')

# Create a function that will register a new user
def registerProperty(Price, address, PostCode, Bedroom, Bathroom, Living_room, Tenure, Tax_Band, Property_Type, EPC_rating):

    #PropertyID = GenPropertyID()

    query = """INSERT INTO PropertyTable (PropertyID, Price, address, PostCode, Bedroom, Bathroom, Living_room, Tenure, Tax_Band, Property_Type, EPC_rating)
                      VALUES (?, ?, ?, ?, ?, ?)"""
    values = (PropertyID, Price, address, PostCode, Bedroom, Bathroom, Living_room, Tenure, Tax_Band, Property_Type, EPC_rating)

    cursor.execute(query, values)

# Create a function that will return the Properties that match the user preferences
def get_Property(Price, address, PostCode, Bedroom, Bathroom, Living_room, Tenure, Tax_Band, Property_Type, EPC_rating):




    query = f"""SELECT UserSalt FROM PropertyTable WHERE Price = ?"""
    cursor.execute(query, (Price,))
    User_salt = cursor.fetchone()






#register('user@example.com', 'abc123', 'hashed_password', 'John', 'Doe', '1234567890')

#CreateUserTable()

#connection.commit()
#cursor.close()
#connection.close()




# Fetch data
#cursor.execute("SELECT * FROM UserTable")
#rows = cursor.fetchall()
#for row in rows:
   # print(row)

# Close the cursor and the connection
#cursor.close()
#connection.close()

print(GenPropertyID())