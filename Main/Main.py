import random
import time

#from Algorithms.mergesort import MergeSort
from Data_Structures.Graph import Graph
from Data_Structures.Matirx import Matrix
from Booking import Booking
from Json import *

def GetPropertyList():
    PropertyList = []
    for house in Property:
        PropertyList.append(house)
    return PropertyList

#Get Property Details
UserID = "User1"
Property = readJson()
PropertyList = GetPropertyList()
SAMPLE_SIZE = 3


def SimpleRandomSample():
    Sample = []
    PopulationSize = len(PropertyList)

    for i in range(SAMPLE_SIZE):
        index = random.randint(0 , PopulationSize - 1)
        SampleUnit = PropertyList[index]
        Sample.append(SampleUnit)

    return Sample


class Display:
    def __init__(self, PropertyList, Property):
        self.PropertyList = PropertyList
        self.LikedProperties = []

        self.SeenList = []
        self.SeenDict = {}

        self.Property = Property

    def DisplayProperty(self, PropertyID):

        Text = f"""Property ID {PropertyID}.
        
                Property Info:
                - Address: {self.Property[PropertyID]["address"]}
                - PostCode: {self.Property[PropertyID]["PostCode"]}
                - Price: {self.Property[PropertyID]["Price"]}
                - Bedrooms: {self.Property[PropertyID]["Bedroom"]}
                - Bathrooms: {self.Property[PropertyID]["Bathroom"]}
                - Living rooms: {self.Property[PropertyID]["living_rooms"]}
                - Tenure:   {self.Property[PropertyID]["tenure"]}
                - Tax Band: {self.Property[PropertyID]["tax_band"]}
                - Property Type: {self.Property[PropertyID]["property_type"]}
                - EPC Rating: {self.Property[PropertyID]["EPC_rating"]}
                """

        Start_time = time.time()
        print("\n##################################################\n")
        print(Text)
        print("\n##################################################\n")

        UserOpinion = input("Do you like the property?  [y/n] ").lower()
        End_time = time.time()

        if UserOpinion == "y":
            self.LikedProperties.append(PropertyID)
            RequestBooking = input("Do you want to book a viewing? [y/n]").lower()

            if RequestBooking == "y":
                booking = Booking(PropertyID)
                while not True:
                    booking.FindAvailability(UserID)

                # Booking procedure

        TimeDuration = End_time - Start_time
        self.SeenList.append(str(PropertyID))
        self.SeenDict[str(PropertyID)] = int(TimeDuration)

        self.RankList()

    def DisplayBooking(self):

    def RankList(self):
        self.SeenList = sorted(self.SeenList, key=lambda ID: self.SeenDict[ID], reverse=True)

#main

def Main():

    Sample = SimpleRandomSample()

    Program = Display(PropertyList, Property)

    for i in range(0,3):
        print(i)
        ID = Sample[i]
        Program.DisplayProperty(ID)

    print(Program.SeenList)
    print(Program.SeenDict)

    graph = Graph(Property)
    matrix = Matrix()
    matrix.AppendMatrix(graph.getmatrix())

    Rank = matrix.GetRank()

    for ID in Rank:
        if ID not in Program.SeenList:
            Program.DisplayProperty(ID)

Main()