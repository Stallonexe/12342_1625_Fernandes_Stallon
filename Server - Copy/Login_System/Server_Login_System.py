import sqlite3


connection = sqlite3.connect('login.db')
cursor = connection.cursor()

# Create a UserTable
def CreateUserTable():

    cursor.execute('''CREATE TABLE IF NOT EXISTS UserTable
                  (
                  UserEmail VARCHAR(320) PRIMARY KEY NOT NULL,
                  UserSalt CHAR(6) NOT NULL,
                  PasswordHash VARCHAR(128) NOT NULL,
                  FirstName VARCHAR(26) NOT NULL,
                  Surname VARCHAR(26) NOT NULL,
                  ContactNo CHAR(11) NOT NULL
                  )''')

# Create a function that will register a new user
def register(UserEmail, UserSalt, PasswordHash, FirstName, Surname, ContactNo, cursor, connection):
    query = """INSERT INTO UserTable (UserEmail, UserSalt, PasswordHash, FirstName, Surname, ContactNo) VALUES (?, ?, ?, ?, ?, ?)"""
    values = (UserEmail, UserSalt, PasswordHash, FirstName, Surname, ContactNo)

    cursor.execute(query, values)
    connection.commit()

# Create a function that will return the Salt registered under the UserEmail
def get_salt(UserEmail, cursor, connection):
    query = """SELECT UserSalt FROM UserTable WHERE UserEmail = ?"""
    cursor.execute(query, (UserEmail,))
    User_salt = cursor.fetchone()

    if len(User_salt) !=0:
        return User_salt[0]
    else:
        return None

# Create a function that check the database if the UserEmail is registered or not.
def verify_email(UserEmail, cursor, connection):
    query = """SELECT UserEmail FROM UserTable WHERE UserEmail = ?"""
    cursor.execute(query, (UserEmail,))
    User_Email = cursor.fetchone() # Store the email address fetched from database

    # compare the Email address, if match: return True
    if (User_Email[0]) == UserEmail:
        return True
    else:
        return False

# Create a function that check the database, if the PasswordHash matches to the one stored on the database.
def verify_hash(UserEmail, PasswordHash, cursor, connection):
    query = """SELECT PasswordHash FROM UserTable WHERE UserEmail = ?"""
    cursor.execute(query, (UserEmail,))
    User_Hash = cursor.fetchone() # Store the PasswordHash fetched from database




    # compare the Password Hash, if match: return True
    if (User_Hash[0]) == PasswordHash:
        return True
    else:
        return False



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
