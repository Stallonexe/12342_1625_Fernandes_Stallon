import sqlite3
from Server.Modules.functions import *

class Property:
    def __init__(self):
        # Database
        self.connection = sqlite3.connect('Database/Property.db')
        self.cursor = self.connection.cursor()

        #Methods
        self.CreatePropertyTable()

    def CreatePropertyTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS PropertyTable
                              (
                              PropertyID VARCHAR(6) PRIMARY KEY NOT NULL,
                              address VARCHAR(320) NOT NULL,
                              postcode CHAR(6) NOT NULL,
                              price INTEGER NOT NULL,
                              bedroom INTEGER NOT NULL,
                              bathroom INTEGER NOT NULL,
                              living_room INTEGER NOT NULL,
                              tenure VARCHAR(18) NOT NULL,
                              tax_band CHAR(1) NOT NULL,
                              property_type VARCHAR(64) NOT NULL,
                              EPC_rating CHAR(1)
                              )''')

    def AddProperty(self, PropertyID, price, address, postcode, bedroom, bathroom, living_room, tenure, tax_band, property_type, EPC_rating ):
        query = """INSERT INTO PropertyTable (PropertyID, price, address, postcode, bedroom, bathroom, living_room, tenure, tax_band, property_type, EPC_rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = (PropertyID, price, address, postcode, bedroom, bathroom, living_room, tenure, tax_band, property_type, EPC_rating,)

        self.cursor.execute(query, values)
        self.connection.commit()

    # Get Functions
    def get_price(self, PropertyID):
        query = """SELECT price FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        price = self.cursor.fetchone()

        return price

    def get_address(self, PropertyID):
        query = """SELECT address FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        address = self.cursor.fetchone()

        return address

    def get_postcode(self, PropertyID):
        query = """SELECT postcode FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        postcode = self.cursor.fetchone()

        return postcode

    def get_bedroom(self, PropertyID):
        query = """SELECT bedroom FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        bedroom = self.cursor.fetchone()

        return bedroom

    def get_bathroom(self, PropertyID):
        query = """SELECT bathroom FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        bathroom = self.cursor.fetchone()

        return bathroom

    def get_living_room(self, PropertyID):
        query = """SELECT living_room FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        living_room = self.cursor.fetchone()

        return living_room

    def get_tenure(self, PropertyID):
        query = """SELECT tenure FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        tenure = self.cursor.fetchone()

        return tenure

    def get_tax_band(self, PropertyID):
        query = """SELECT tax_band FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        tax_band = self.cursor.fetchone()

        return tax_band

    def get_property_type(self, PropertyID):
        query = """SELECT property_type FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        property_type = self.cursor.fetchone()

        return property_type

    def get_EPC_rating(self, PropertyID):
        query = """SELECT EPC_rating FROM PropertyTable WHERE PropertyID = ?"""
        self.cursor.execute(query, (str(PropertyID),))
        EPC_rating = self.cursor.fetchone()

        return EPC_rating

    def GetProperty(self,UserID, max_price, min_price, postcode, bedroom, bathroom, living_room, tenure,property_type):

        PropertyIDList = self.GetPreferredPropertyIDList(max_price, min_price, postcode, bedroom, bathroom, living_room, tenure,property_type)

        self.Property = {}

        for PropertyID_tuple in PropertyIDList:
            PropertyID = PropertyID_tuple[0]  # Extracting the PropertyID from the tuple
            self.Property[PropertyID] = {}  # Creating a dictionary entry with the extracted PropertyID as the key

            address = self.get_address(PropertyID)
            postcode = self.get_postcode(PropertyID)
            price = self.get_price(PropertyID)
            bedroom = self.get_bedroom(PropertyID)
            bathroom = self.get_bathroom(PropertyID)
            living_room = self.get_living_room(PropertyID)
            tenure = self.get_tenure(PropertyID)
            tax_band = self.get_tax_band(PropertyID)
            property_type = self.get_property_type(PropertyID)
            EPC_rating = self.get_EPC_rating(PropertyID)

            self.Property[PropertyID]["address"] = address[0]
            self.Property[PropertyID]["PostCode"] = postcode[0]
            self.Property[PropertyID]["Price"] = price[0]
            self.Property[PropertyID]["Bedroom"] = bedroom[0]
            self.Property[PropertyID]["Bathroom"] = bathroom[0]
            self.Property[PropertyID]["living_rooms"] = living_room[0]
            self.Property[PropertyID]["tenure"] = tenure[0]
            self.Property[PropertyID]["tax_band"] = tax_band[0]
            self.Property[PropertyID]["property_type"] = property_type[0]
            self.Property[PropertyID]["EPC_rating"] = EPC_rating[0]

        filepath = f"JsonFiles/{UserID}.json"
        #g = 'Server/Data/JsonFiles'
        writeJson(self.Property, filepath)

        return True

    def GetPreferredPropertyIDList(self, max_price, min_price, postcode, bedroom, bathroom, living_room, tenure,
                                   property_type):
        query = """SELECT PropertyID FROM PropertyTable 
             WHERE price BETWEEN ? AND ? 
             AND postcode LIKE ? || '%'
             AND bedroom <= ? 
             AND bathroom <= ? 
             AND living_room <= ? 
             AND tenure = ? 
             AND property_type = ?"""

        values = (min_price, max_price, postcode[:2], bedroom, bathroom, living_room, tenure, property_type,)

        self.cursor.execute(query, values)

        PropertyIDs = []
        for row in self.cursor.fetchall():
            PropertyIDs.append(row)

        return PropertyIDs

    #set functions (Sets the value of attributes for a given object)

    def set_price(self, new_price, PropertyID):
        query = """UPDATE PropertyTable SET price = ? WHERE property_id = ?"""
        values = (new_price, PropertyID,)

        self.cursor.execute(query, values)
        self.connection.commit()

House = Property()
House.AddProperty('H1', 435000, '3 Potters Road', 'UB24AS', 2, 2, 1, 'FREEHOLD', 'C', 'TERRACED', 'A')
House.AddProperty('H2', 450000, '1 Potters Road', 'UB24AS', 2, 2, 1, 'FREEHOLD', 'C', 'TERRACED', 'A')
House.AddProperty('H3', 425000, '17 Potters Road', 'UB24AS', 2, 2, 1, 'FREEHOLD', 'C', 'TERRACED', 'A')

House.GetProperty('U1', 500000, 0, 'UB', 2, 2, 1, 'FREEHOLD', 'TERRACED')