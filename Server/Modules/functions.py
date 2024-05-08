import json

def writeJson(Dictionary, filename):
    with open(filename,'w') as json_file:
        json.dump(Dictionary, json_file)
    json_file.close()

def readJson(filename):
    with open(filename,'r') as json_file:
        Dictionary = json.load(json_file)
    json_file.close()
    return Dictionary
