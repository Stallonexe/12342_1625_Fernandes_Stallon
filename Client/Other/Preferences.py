import math

class Users:
  def __init__(self, User_email, **preference):
    self.email = User_email

    #max price
    try:
      self.max_price = preference["max_price"]
    except:
      self.max_price = -1

    #min price
    try:
      self.min_price = preference["min_price"]
    except:
      self.min_price = -1

    #location
    try:
      self.postcode = preference["postcode"]
    except:
      self.postcode = -1

    #bedroom
    try:
      self.bedroom = preference["bedroom"]
    except:
      self.bedroom = -1

    #bedroom
    try:
      self.bedroom = preference["bedroom"]
    except:
      self.bedroom = -1

    #bathroom
    try:
      self.bathroom = preference["bathroom"]
    except:
      self.bathroom = -1

    #living rooms
    try:
      self.living_rooms = preference["living_rooms"]
    except:
      self.living_rooms = -1

    #property type
    try:
      self.property_type = preference["property_type"]
    except:
      self.property_type = -1

  def SavePreferences(self):
      with open("Preferences.txt","w") as file:
          



    print(self.living_rooms)



denzil = Users("denzil@gmail.com", living_rooms = 5)



def Sigmoid(x):
  u = 1 # numerator
  v = 1 + ((math.e) ** -x)
  return u / v

def calc_weight(User, Property):


print(Sigmoid(10))

