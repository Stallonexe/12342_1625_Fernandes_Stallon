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
        if self.Property[HeadNode]["PostCode"][:2] == self.Property[TailNode]["PostCode"][:2]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if self.Property[HeadNode]["Bedroom"] == self.Property[TailNode]["Bedroom"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if self.Property[HeadNode]["Bathroom"] == self.Property[TailNode]["Bathroom"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if self.Property[HeadNode]["living_rooms"] == self.Property[TailNode]["living_rooms"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)


        if self.Property[HeadNode]["tax_band"] == self.Property[TailNode]["tax_band"]:
            self.__addlink(HeadNode, TailNode)
            self.__addlink(TailNode, HeadNode)

        if self.Property[HeadNode]["property_type"] == self.Property[TailNode]["property_type"]:
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




#CreateGraph()
