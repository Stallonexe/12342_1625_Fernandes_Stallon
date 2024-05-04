import random
import json
import time

from Algorithms.mergesort import MergeSort

PropertyList = []

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

    def DisplayProperty(self, PropertyID):

        Text = f"""Property ID {PropertyID}.
        
                Property Info:
                - Address: {self.Property["address"]}
                - PostCode: {self.Property["PostCode"]}
                - Price: {self.Property["Price"]}
                - Bedrooms: {self.Property["Bedroom"]}
                - Bathrooms: {self.Property["Bathroom"]}
                - Living rooms: {self.Property["living_rooms"]}
                - Tenure:   {self.Property["tenure"]}
                - Tax Band: {self.Property["tax_band"]}
                - Property Type: {self.Property["property_type"]}
                - EPC Rating: {self.Property["EPC_rating"]}
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


    def ReadJsonFile(self):

        with open("Properties.json", "r") as json_file:
            self.Property = json.load(json_file)

    def RankList(self):
        self.TimeList = list(self.SeenDict.values())
        self.TimeList = MergeSort(self.TimeList)


        # Use merge sort or other


