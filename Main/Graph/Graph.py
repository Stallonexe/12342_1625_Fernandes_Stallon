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

for ID in Property:
    graph[ID] = {}
    print(graph)

for HeadNode in Property:
    for TailNode in Property:
        print(f"graph[{HeadNode}][{TailNode}]")
        if HeadNode != TailNode:

            if TailNode not in graph[HeadNode]:
                if Property[HeadNode]["PostCode"][:2] == Property[TailNode]["PostCode"][:2]:
                    graph[HeadNode][TailNode] = 1

                if Property[HeadNode]["Bedroom"] == Property[TailNode]["Bedroom"]:
                    graph[HeadNode][TailNode] = 1


                if Property[HeadNode]["Bathroom"] == Property[TailNode]["Bathroom"]:
                    graph[HeadNode][TailNode] = 1


                if Property[HeadNode]["living_rooms"] == Property[TailNode]["living_rooms"]:
                    graph[HeadNode][TailNode] = 1


                if Property[HeadNode]["tax_band"] == Property[TailNode]["tax_band"]:
                    graph[HeadNode][TailNode] = 1


                if Property[HeadNode]["property_type"] == Property[TailNode]["property_type"]:
                    graph[HeadNode][TailNode] = 1
        else:
            graph[HeadNode][TailNode] = 0

