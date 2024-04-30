class Property:
    def __init__(self, price, address, postcode, bedroom, bathroom, living_room, tenure, tax_band, property_type, EPC_rating, cursor, connection):
        # Attributes
        self.price = price
        self.address = address
        self.postcode = postcode
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.living_room = living_room
        self.tenure = tenure
        self.tax_band = tax_band
        self.property_type = property_type
        self.EPC_rating = EPC_rating

        # Database
        self.cursor = cursor
        self.connection = connection

        #Methods
        self.CreatePropertyTable()

    def CreatePropertyTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS PropertyTable
                              (
                              address VARCHAR(320) PRIMARY KEY NOT NULL,
                              postcode CHAR(6) PRIMARY KEY NOT NULL,
                              price INTEGER NOT NULL,
                              bedroom INTEGER) NOT NULL,
                              bathroom INTEGER NOT NULL,
                              living_room INTEGER NOT NULL,
                              tenure VARCHAR(18) NOT NULL,
                              tax_band CHAR(a) NOT NULL,
                              property_type VARCHAR(64) NOT NULL,
                              EPC_rating CHAR(1)
                              
                              )''')

    # Get Functions
    def get_price(self):
        return self.price

    def get_address(self):
        return self.address

    def get_postcode(self):
        return self.postcode

    def get_bedroom(self):
        return self.bedroom

    def get_bathroom(self):
        return self.bathroom

    def get_living_room(self):
        return self.living_room

    def get_tenure(self):
        return self.tenure

    def get_tax_band(self):
        return self.tax_band

    def get_property_type(self):
        return self.property_type

    def get_EPC_rating(self):
        return self.EPC_rating

  #set functions (Sets the value of attributes for a given object)

    def set_price(self,price):
        self.price = price

    def set_address(self,address):
        self.address = address

    def set_postcode(self,postcode):
        self.postcode = postcode

    def set_bedroom(self,bedroom):
        self.bedroom = bedroom

    def set_bathroom(self,bathroom):
        self.bathroom = bathroom

    def set_living_room(self, living_room):
        self.living_room = living_room

    def set_tenure(self, tenure):
        self.tenure = tenure

    def set_tax_band(self, tax_band):
        self.tax_band = tax_band

    def set_property_type(self, property_type):
        self.property_type = property_type

    def set_EPC_rating(self,EPC_rating):
        return self.EPC_rating


Property1 = Property(450000, "1 Potters Road", "UB24AS", 2, 2, 1, "freehold", "C", "terraced", "B")


print(Property1.get_price())
print(Property1.get_address())
print(Property1.get_postcode())
print(Property1.get_bedroom())
print(Property1.get_bathroom())
print(Property1.get_living_room())
print(Property1.get_tenure())
print(Property1.get_property_type())
print(Property1.get_EPC_rating())


#def generate_card():
  #

#def display_card():
  #

#def display_information():
  #
