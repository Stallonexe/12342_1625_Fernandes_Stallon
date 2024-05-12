import random
from Commands import decoder
import string


streetAddresses = [
    "123MainStreet",
    "456ElmStreet",
    "789MapleAvenue",
    "101OakLane",
    "202ineRoad",
    "303CedarCourt",
    "404WalnutBoulevard",
    "505BirchAvenue",
    "606pruceDrive",
    "707PillowLane",
    "808herryStreet",
    "909MagnoliaDrive",
    "111MinecrestAvenue",
    "222RiverRoad",
    "333LakeviewDrive",
    "444SunsetBoulevard",
    "555ForestLane",
    "666RidgecrestDrive",
    "777MeadowbrookCourt",
    "888arkAvenue",
    "999SpringStreet",
    "1210LaurelLane",
    "1311ElmwoodAvenue",
    "1412SycamoreStreet",
    "1513CedarAvenue",
    "1614OakStreet",
    "1715MapleLane",
    "1816PineDrive",
    "1917BirchCourt",
    "2018SpruceAvenue",
    "2119WillowRoad",
    "2220CherryLane",
    "2321MagnoliaCourt",
    "2422PinecrestDrive",
    "2523RiverLane",
    "2624LakeviewCourt",
    "2725SunsetAvenue",
    "2826ForestDrive",
    "2927RidgeRoad",
    "3028MeadowbrookAvenue",
    "3129ParkLane",
    "3230SpringCourt",
    "3331LaurelAvenue",
    "3432ElmLane",
    "3533SycamoreDrive",
    "3634CedarCourt",
    "3735OakAvenue",
    "3836MapleRoad",
    "3937PineStreet",
    "4038BirchLane",
    "4139SpruceBoulevard",
    "4240WillowDrive",
    "4341CherryAvenue",
    "4442 MagnoliaStreet",
    "4543PinecrestLane",
    "4644RiverDrive",
    "4745LakeviewBoulevard",
    "4846SunsetLane",
    "4947ForestAvenue",
    "5048RidgeLane",
    "5149MeadowbrookStreet",
    "5250ParkDrive",
    "5351SpringAvenue",
    "5452LaurelRoad",
    "5553ElmwoodCourt",
    "5654SycamoreLane",
    "5755CedarDrive",
    "5856OakBoulevard",
    "9577MapleAvenue",
    "6058PineLane",
    "6155BirchStreet",
    "6260SpruceCourt",
    "6361WillowAvenue",
    "6462CherryRoad",
    "6563 MagnoliaLane",
    "6664PinecrestBoulevard",
    "6765RiverAvenue",
    "6866 LakeviewDrive",
    "6967SunsetCourt",
    "7068 ForestLane",
    "7169RidgecrestAvenue",
    "7270MeadowbrookRoad",
    "7371ParkCourt",
    "7472SpringStreet",
    "7573LaurelDrive",
    "7674ElmLane",
    "7775SycamoreAvenue",
    "7876CedarRoad",
    "7977OakCourt",
    "8078MapleDrive",
    "8179PinecrestLane",
    "8280BirchBoulevard",
    "8381SpruceAvenue",
    "8482WillowLane",
    "8583CherryDrive",
    "8684MagnoliaCourt",
    "8785PineRoad",
    "8886RiverStreet",
    "8986LakeviewLane",
    "9088SunsetDrive",
    "9189ForestAvenue",
    "9290RidgeDrive",
    "9391MeadowbrookLane",
    "9492ParkAvenue",
    "9593SpringLane",
    "9694LaurelBoulevard",
    "9795ElmStreet",
    "9896SycamoreDrive",
    "9997CedarAvenue",
    "10098OakLane"
]


def generate_property_id(count):
    return f"H{count}"

def generate_price():
    return round(random.randint(100000, 1000000))

def generate_address():
    return random.choice(streetAddresses)

def generate_postcode():
    postcodes = ["HA04YF", "UB13AD", "E152DA", "N12RT", "SW1A1AA", "W112BQ", "UB24AS", "HA9ONB", "SN10"]
    return random.choice(postcodes)

def generate_bedroom_no():
    return random.randint(1, 5)

def generate_bathroom_no():
    return random.randint(1, 3)

def generate_livingroom_no():
    return random.randint(1, 3)

def generate_tenure():
    return random.choice(["FREEHOLD", "LEASEHOLD"])

def generate_tax_band():
    return random.randint(1, 10)

def generate_property_type():
    property_types = ["Detached", "SemiDetached", "Terraced", "Apartment", "Flat", "Bungalow"]
    return random.choice(property_types)

def generate_epc_rating():
    return random.choice(["A", "B", "C", "D", "E", "F", "G"])

def create_sample_properties(num_properties):
    for i in range(1, num_properties + 1):
        PropertyID = generate_property_id(i)  # Use i as count
        price = generate_price()
        address = generate_address()
        postcode = generate_postcode()
        BedroomNo = generate_bedroom_no()
        BathroomNo = generate_bathroom_no()
        LivingroomNo = generate_livingroom_no()
        tenure = generate_tenure()
        tax_band = generate_tax_band()
        property_type = generate_property_type()
        epc_rating = generate_epc_rating()

        command = f"Create RegProperty {PropertyID} {price} {address} {postcode} {BedroomNo} {BathroomNo} {LivingroomNo} {tenure} {tax_band} {property_type} {epc_rating}"
        decoder.execute(command)
        #print(command)

for i in range(101):
    create_sample_properties(i)
