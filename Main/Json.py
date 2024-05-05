import json

def writeJson(Dictionary, filename):
    with open(f"{filename}.json","w") as json_file:
        json.dump(Dictionary, json_file)
    json_file.close()

def readJson(filename):
    with open(f"{filename}.json","r") as json_file:
        Dictionary = json.load(json_file)
    json_file.close()
    return Dictionary


