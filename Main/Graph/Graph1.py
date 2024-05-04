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
            "living_rooms": 3,
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
            "Bathroom": 10,
            "living_rooms": 4,
            "tenure": "Freehold",
            "tax_band": "E",
            "property_type": "House",
            "EPC_rating": "D"
        }
}

class Graph:
    def __init__(self, PropertyDict):
        self.Property = PropertyDict

        self.graph = {}
        self.Matrix = {}

        self.MainProcedure()

    def MainProcedure(self):
        self.LoadGraph()
        for Head in self.Property:
            for Tail in self.Property:
                if Head != Tail:
                    self.findlink(Head, Tail)
        self.addweights()

    def LoadGraph(self):
        for i in self.Property:
            self.graph[i] = {}
            for j in self.Property:
                self.graph[i][j] = 0

    def set_root_node(self, root_node):
        self.startnode = root_node

    def findlink(self, HeadNode, TailNode):
        if Property[HeadNode]["PostCode"][:2] == Property[TailNode]["PostCode"][:2]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if Property[HeadNode]["Bedroom"] == Property[TailNode]["Bedroom"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if Property[HeadNode]["Bathroom"] == Property[TailNode]["Bathroom"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if Property[HeadNode]["living_rooms"] == Property[TailNode]["living_rooms"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)


        if Property[HeadNode]["tax_band"] == Property[TailNode]["tax_band"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if Property[HeadNode]["property_type"] == Property[TailNode]["property_type"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)


    def __addlink(self, HeadNode, TailNode):
        self.graph[HeadNode][TailNode] += 0.5

    def addweights(self):
        for HeadNode in self.graph:
            OutboundLinks = 0
            for links in self.graph[HeadNode].values():
                OutboundLinks += links
            #print(f"{HeadNode}: {OutboundLinks}")

            Weight = 1 / OutboundLinks

            for TailNode in self.graph:
                self.graph[HeadNode][TailNode] *= Weight

    def getmatrix(self):
        for Head in self.Property:
            values = []
            for value in self.graph[Head].values():
                values.append(value)
            self.Matrix[Head] = values
        return self.Matrix










def CreateGraph():
    graph = Graph(Property)

    print(graph.graph)
    print()




    for HeadNode in Property:
        print(f"{HeadNode}: {graph.graph[HeadNode]}")

    print()

    print(graph.getmatrix())




CreateGraph()
