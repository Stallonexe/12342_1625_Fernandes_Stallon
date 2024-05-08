import sqlite3

class Property:
    def __init__(self, PropertyID, price, address, postcode, bedroom, bathroom, living_room, tenure, tax_band, property_type, EPC_rating):
        # Attributes
        self.PropertyID = PropertyID
        self.price = int(price)
        self.address = address
        self.postcode = postcode
        self.bedroom = int(bedroom)
        self.bathroom = int(bathroom)
        self.living_room = int(living_room)
        self.tenure = tenure
        self.tax_band = tax_band
        self.property_type = property_type
        self.EPC_rating = EPC_rating

        # Database
        self.connection = sqlite3.connect('Property.db')
        self.cursor = self.connection.cursor()

        #Methods
        self.CreatePropertyTable()
        self.AddProperty()

    def CreatePropertyTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS PropertyTable
                              (
                              PropertyID CHAR(6) PRIMARY KEY NOT NULL,
                              address VARCHAR(320) NOT NULL,
                              postcode CHAR(6) UNIQUE NOT NULL,
                              price INTEGER NOT NULL,
                              bedroom INTEGER NOT NULL,
                              bathroom INTEGER NOT NULL,
                              living_room INTEGER NOT NULL,
                              tenure VARCHAR(18) NOT NULL,
                              tax_band CHAR(1) NOT NULL,
                              property_type VARCHAR(64) NOT NULL,
                              EPC_rating CHAR(1)
                              )''')

    def AddProperty(self):
        query = """INSERT INTO PropertyTable (PropertyID, price, address, postcode, bedroom, bathroom, living_room, tenure, tax_band, property_type, EPC_rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = (self.PropertyID, self.price, self.address, self.postcode, self.bedroom, self.bathroom, self.living_room, self.tenure, self.tax_band, self.property_type, self.EPC_rating)

        self.cursor.execute(query, values)
        self.connection.commit()

    # Get Functions
    def get_price(self, PropertyID):
        query = """SELECT price FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        price = self.cursor.fetchone()

        return price

    def get_address(self, PropertyID):
        query = """SELECT address FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        address = self.cursor.fetchone()

        return address

    def get_postcode(self, PropertyID):
        query = """SELECT postcode FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        postcode = self.cursor.fetchone()

        return postcode

    def get_bedroom(self, PropertyID):
        query = """SELECT bedroom FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        bedroom = self.cursor.fetchone()

        return bedroom

    def get_bathroom(self, PropertyID):
        query = """SELECT bathroom FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        bathroom = self.cursor.fetchone()

        return bathroom

    def get_living_room(self, PropertyID):
        query = """SELECT living_room FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        living_room = self.cursor.fetchone()

        return living_room

    def get_tenure(self, PropertyID):
        query = """SELECT tenure FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        tenure = self.cursor.fetchone()

        return tenure

    def get_tax_band(self, PropertyID):
        query = """SELECT tax_band FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        tax_band = self.cursor.fetchone()

        return tax_band

    def get_property_type(self, PropertyID):
        query = """SELECT property_type FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        property_type = self.cursor.fetchone()

        return property_type

    def get_EPC_rating(self, PropertyID):
        query = """SELECT EPC_rating FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (PropertyID,))
        EPC_rating = self.cursor.fetchone()

        return EPC_rating

    def GetProperty(self, PropertyID):
        price = self.get_price(PropertyID)
        address = self.get_address(PropertyID)
        postcode = self.get_postcode(PropertyID)
        bedroom = self.get_bedroom(PropertyID)
        bathroom = self.get_bathroom(PropertyID)
        living_room = self.get_living_room(PropertyID)
        tenure = self.get_tenure(PropertyID)
        tax_band = self.get_tax_band(PropertyID)
        property_type = self.get_property_type(PropertyID)
        EPC_rating = self.get_EPC_rating(PropertyID)


        return f"{price} {address} {postcode} {bedroom} {bathroom} {living_room} {tenure} {tax_band} {property_type} {EPC_rating}"

    def GetPreferredPropertyID(self, max_price, min_price, postcode, bedroom, bathroom, living_room, tenure,
                               property_type):
        query = """SELECT PropertyID FROM PropertyTable 
             WHERE Price BETWEEN? AND? 
             AND Postcode =? 
             AND Bedrooms <=? 
             AND Bathrooms <=? 
             AND LivingRooms <=? 
             AND Tenure =? 
             AND PropertyType =?"""

        values = (min_price, max_price, postcode, bedroom, bathroom, living_room, tenure, property_type)

        self.cursor.execute(query, values)

        PropertyIDs = []
        for row in self.cursor.fetchall():
            PropertyIDs.append(row)

        return PropertyIDs


  #set functions (Sets the value of attributes for a given object)

    def set_price(self, new_price, PropertyID):
        query = """UPDATE PropertyTable SET price = ? WHERE property_id = ?"""
        values = (new_price, PropertyID)

        self.cursor.execute(query, values)
        self.connection.commit()

House = property()