Property = {
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


def create_links(Property):
    graph = {}

    # Initialize the graph with nodes for each property
    for house in Property:
        graph[house] = {}

    # Compare each property with every other property
    for house1 in Property:
        for house2 in Property:
            if house1 != house2:
                # Check for similarities
                if Property[house1]["PostCode"][:2] == Property[house2]["PostCode"][:2]:
                    graph[house1][house2] = "Same PostCode Prefix"

                if Property[house1]["Price"] == Property[house2]["Price"]:
                    graph[house1][house2] = "Same Price"

                if Property[house1]["Bedroom"] == Property[house2]["Bedroom"]:
                    graph[house1][house2] = "Same Number of Bedrooms"
                # Add more conditions for other similarities if needed

    return graph


# Test the function
graph = create_links(Property)
print(graph)
