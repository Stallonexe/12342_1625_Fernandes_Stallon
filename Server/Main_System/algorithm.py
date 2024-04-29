from DataStructures import *
from Properties import Property



def LoadProperties():
    A = Property(450000, "1 Potters Road", "UB24AS", 2, 2, 1, "freehold", "C", "terraced", "B")


def CreateGraph():
    
    graph = Graph()

graph.set_startnode('A')
graph.set_targetnode('E')
graph.addnode('A', {'B': 4, 'C': 2})
graph.addnode('B', {'A': 4, 'C': 1, 'D': 5})
graph.addnode('C', {'A': 2, 'B': 1, 'D': 8, 'E': 10})
graph.addnode('D', {'B': 5, 'C': 8, 'E': 2, 'Z': 6})
graph.addnode('E', {'C': 10, 'D': 2, 'Z': 5})
graph.addnode('Z', {'D': 6, 'E': 5})

print(graph.graph)


def Click():
