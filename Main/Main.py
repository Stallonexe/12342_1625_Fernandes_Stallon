import random
import json
import time

from Algorithms.mergesort import MergeSort

PropertyList = ["H1","H2","H3","H4","H5","H6"]

#Get Property Details


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
    def __init__(self, Sample, PropertyList):
        self.Sample = Sample
        self.PropertyList = PropertyList
        self.LikedProperties = []

        self.SeenList = []
        self.SeenDict = {}
        self.Test() # remove later

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
                print("ello")
                # Booking procedure

        TimeDuration = End_time - Start_time
        self.SeenList.append(str(PropertyID))
        self.SeenDict[str(PropertyID)] = int(TimeDuration)

        self.RankList()


    def ReadJsonFile(self):

        with open("Properties.json", "r") as json_file:
            self.Property = json.load(json_file)

    def Test(self):
        self.Property = {
            "H1": {
                "address": "123 Main St",
                "PostCode": "AB12 3CD",
                "Price": 250000,
                "Bedroom": 3,
                "Bathroom": 2,
                "living_rooms": 1,
                "tenure": "Freehold",
                "tax_band": "C",
                "property_type": "House",
                "EPC_rating": "B"
            },
            "H2": {
                "address": "456 Elm St",
                "PostCode": "EF34 5GH",
                "Price": 300000,
                "Bedroom": 4,
                "Bathroom": 3,
                "living_rooms": 2,
                "tenure": "Leasehold",
                "tax_band": "D",
                "property_type": "Apartment",
                "EPC_rating": "C"
            },
            "H3": {
                "address": "789 Oak St",
                "PostCode": "IJ56 7KL",
                "Price": 200000,
                "Bedroom": 2,
                "Bathroom": 1,
                "living_rooms": 1,
                "tenure": "Freehold",
                "tax_band": "B",
                "property_type": "Flat",
                "EPC_rating": "A"
            },
            "H4": {
                "address": "10 Maple St",
                "PostCode": "MN78 9OP",
                "Price": 350000,
                "Bedroom": 5,
                "Bathroom": 3,
                "living_rooms": 2,
                "tenure": "Freehold",
                "tax_band": "E",
                "property_type": "House",
                "EPC_rating": "D"
            },
            "H5": {
                "address": "11 Pine St",
                "PostCode": "QR90 1ST",
                "Price": 280000,
                "Bedroom": 3,
                "Bathroom": 2,
                "living_rooms": 1,
                "tenure": "Leasehold",
                "tax_band": "C",
                "property_type": "Flat",
                "EPC_rating": "B"
            },
            "H6": {
                "address": "12 Cedar St",
                "PostCode": "UV23 4WX",
                "Price": 400000,
                "Bedroom": 4,
                "Bathroom": 3,
                "living_rooms": 2,
                "tenure": "Freehold",
                "tax_band": "F",
                "property_type": "House",
                "EPC_rating": "C"
            }
        }

    def RankList(self):
        self.SeenList = sorted(self.SeenList, key=lambda ID: self.SeenDict[ID], reverse=True)
        # Use merge sort or other

#main

Sample = SimpleRandomSample()

Program = Display(Sample, PropertyList)

for i in range(0,3):
    ID = Sample[i]
    Program.DisplayProperty(ID)

print(Program.SeenList)
print(Program.SeenDict)