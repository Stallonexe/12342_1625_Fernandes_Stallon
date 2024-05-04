Property = {
        "H1": {
            "address": "123 Main St",
            "PostCode": "HA12 3CD",
            "Price": 250000,
            "Bedroom": 2,
            "Bathroom": 2,
            "living_rooms": 1,
            "tenure": "Freehold",
            "tax_band": "C",
            "property_type": "Detached",
            "EPC_rating": "B"
        },
        "H2": {
            "address": "456 Elm St",
            "PostCode": "UB34 5GH",
            "Price": 300000,
            "Bedroom": 2,
            "Bathroom": 3,
            "living_rooms": 2,
            "tenure": "Leasehold",
            "tax_band": "D",
            "property_type": "Apartment",
            "EPC_rating": "C"
        },
        "H3": {
            "address": "789 Oak St",
            "PostCode": "HA56 7KL",
            "Price": 200000,
            "Bedroom": 3,
            "Bathroom": 1,
            "living_rooms": 1,
            "tenure": "Freehold",
            "tax_band": "B",
            "property_type": "Flat",
            "EPC_rating": "A"
        },
        "H4": {
            "address": "10 Maple St",
            "PostCode": "HA78 9OP",
            "Price": 350000,
            "Bedroom": 2,
            "Bathroom": 3,
            "living_rooms": 2,
            "tenure": "Freehold",
            "tax_band": "E",
            "property_type": "House",
            "EPC_rating": "D"
        }
}


graph = {}

PropertyList = ["H1", "H2", "H3", "H4", "H5", "H6"]

def FindLink():

    for House in Property:
        graph[House] = {}

    for House1 in Property:
        for House2 in Property:

            if House1 != House2:
                print(graph)
                if Property[House1]["PostCode"][:2] == Property[House2]["PostCode"][:2]:
                    if House2 in graph[House1]:
                        graph[House1][House2] += 1
                        graph[House2][House1] += 1
                    else:
                        graph[House1][House2] = 1
                        graph[House2][House1] = 1

                if Property[House1]["Bedroom"] == Property[House2]["Bedroom"]:
                    if House2 in graph[House1] and House1 in graph[House2]:
                        graph[House1][House2] += 1
                        graph[House2][House1] += 1
                    else:
                        graph[House1][House2] = 1
                        graph[House2][House1] = 1

                if Property[House1]["Bathroom"] == Property[House2]["Bathroom"]:
                    if House2 in graph[House1] and House1 in graph[House2]:
                        graph[House1][House2] += 1
                        graph[House2][House1] += 1
                    else:
                        graph[House1][House2] = 1
                        graph[House2][House1] = 1

                if Property[House1]["living_rooms"] == Property[House2]["living_rooms"]:
                    if House2 in graph[House1] and House1 in graph[House2]:
                        graph[House1][House2] += 1
                        graph[House2][House1] += 1
                    else:
                        graph[House1][House2] = 1
                        graph[House2][House1] = 1

                if Property[House1]["tax_band"] == Property[House2]["tax_band"]:
                    if House2 in graph[House1] and House1 in graph[House2]:
                        graph[House1][House2] += 1
                        graph[House2][House1] += 1
                    else:
                        graph[House1][House2] = 1
                        graph[House2][House1] = 1

                if Property[House1]["tax_band"] == Property[House2]["tax_band"]:
                    if House2 in graph[House1] and House1 in graph[House2]:
                        graph[House1][House2] += 1
                        graph[House2][House1] += 1
                    else:
                        graph[House1][House2] = 1
                        graph[House2][House1] = 1

                if Property[House1]["property_type"] == Property[House2]["property_type"]:
                    if House2 in graph[House1] and House1 in graph[House2]:
                        graph[House1][House2] += 1
                        graph[House2][House1] += 1
                    else:
                        graph[House1][House2] = 1
                        graph[House2][House1] = 1

FindLink()
print(graph)

def CalculateWeights():

    for Head in graph.keys():
        OutBoundLinks = len(graph[Head])
        #print(OutBoundLinks)
        Weight = 1 / OutBoundLinks

        #print(graph[Head])

        for Tail in graph[Head].keys():
            graph[Head][Tail] = Weight


CalculateWeights()
print(graph)