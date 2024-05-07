class Graph:
    def __init__(self, Root_node, Samplelist, PropertyDict):

        self.Sample = Samplelist
        self.root = Root_node
        self.Property = PropertyDict.copy()

        self.graph = {}
        self.Matrix = {}


        self.FilterDictionary() #Change
        self.MainProcedure()

    def MainProcedure(self):
        self.LoadGraph()
        for Head in self.Property:
            for Tail in self.Property:
                if Head != Tail:
                    self.findlink(Head, Tail)
        self.addweights()
    #change start
    def FilterDictionary(self):
        print(self.Property)
        print(self.Sample)
        for SampleNode in self.Sample:
            if SampleNode != self.root:
                del self.Property[SampleNode]

                print(self.Property)
                print(self.Sample)

    def LoadGraph(self):
        for i in self.Property:
            self.graph[i] = {}
            for j in self.Property:
                self.graph[i][j] = 0
    #End Change


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

            if OutboundLinks == 0:
                Weight = 0
            else:
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




