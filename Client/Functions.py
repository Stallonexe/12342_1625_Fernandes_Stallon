import json
import csv
import random
import hashlib

from Data_Structures.Graph import Graph
from Data_Structures.Matirx import Matrix


def writeJson(Dictionary, filename):
    with open(filename,'w') as json_file:
        json.dump(Dictionary, json_file)
    json_file.close()

def readJson(filename):
    with open(filename,'r') as json_file:
        Dictionary = json.load(json_file)
    json_file.close()
    return Dictionary

def gen_salt():
    # temp stores hex in the array
    hex_array = []
    for i in range(4):
        #generate random decimal value
        random_value = random.randrange(0,15,1)

        #convert decimal to hexadecimal
        hex_code = hex(random_value)[2:]
        hex_array.append(hex_code)

    #Convert array into a string
    Salt = ''.join(hex_array)
    return Salt

def HashPassword(UserSalt, Password):
    #Get Salt
    Password += UserSalt
    PasswordBytes = Password.encode('utf-8')

    SHA256 = hashlib.sha256()
    SHA256.update(PasswordBytes)
    HashedPassword = SHA256.hexdigest()

    return HashedPassword

def GetPropertyList(Property):
    PropertyList = []
    for house in Property:
        PropertyList.append(house)
    return PropertyList

def PostCode(location):
    FILEPATH = 'Files/PostCode.csv'
    with open(FILEPATH,'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if location.lower() == row[1].lower() and len(location) > 2:
                return row[0]
            elif location[:2].upper() == row[0] and len(location) <= 2:
                return row[1]
        file.close()

def SimpleRandomSample(PropertyList, SAMPLE_SIZE):
    Sample = []
    PopulationSize = len(PropertyList)

    while len(Sample) != 3:
        index = random.randint(0, PopulationSize - 1)
        SampleUnit = PropertyList[index]

        if SampleUnit not in Sample:
            Sample.append(SampleUnit)

    return Sample

def ShowProperties(PropertyList, Property):
    SAMPLE_SIZE = 3
    Sample = SimpleRandomSample(PropertyList, SAMPLE_SIZE)


def RomoveRoot(Root, PropertyList):
    index = PropertyList.index(Root)

    del PropertyList[index]

    return PropertyList


def CompareRanking(Rank1, Rank2, Rank3):
    FinalRank = []
    for index in range(0, len(Rank1)):

        if Rank1[index] == Rank2[index]:
            FinalRank.append(Rank1[index])

        elif Rank2[index] == Rank3[index]:
            FinalRank.append(Rank1[index])

        elif Rank1[index] == Rank3[index]:
            FinalRank.append(Rank1[index])

    return FinalRank





