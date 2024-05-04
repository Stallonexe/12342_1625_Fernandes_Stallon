class PriorityQueue:
    def __init__(self):
        self.queue = {}  # initialise the Queue Dictionary

    def isEmpty(self):
        # The function isEmpty() checks if Queue is Empty

        if len(self.queue) == 0:
            return True
        else:
            return False

    def enQueue(self, key, value):
        # The function enQueue adds the key: value to the Queue dictionary and returns the Queue

        self.queue[str(key)] = value
        return self.queue

    def deQueue(self):
        # The function deQueue removes the key: value from the Queue dictionary and returns the removed element

        if self.isEmpty() is False:
            first_key = list(self.queue)[0]
            value = self.queue.pop(first_key)
            return {first_key: value}
        else:
            return None

    def sortQueue(self):
        # The function
        self.queue = dict(sorted(self.queue.items(), key=lambda element: element[1]))


class Graph:
    def __init__(self):
        self.graph = {}
        self.table = {}
        self.startnode = ""
        self.INF = 100

    def set_startnode(self, startnode):
        self.startnode = startnode

    def addnode(self, node, connectednodes):
        self.graph[node] = connectednodes

        if node == self.startnode:
            self.table[node] = {'Cost': 0, 'Previous_node': ''}
        else:
            self.table[node] = {'Cost': self.INF, 'Previous_node': ''}

    def update(self, node, connectednodes):
        self.graph[str(node)] = connectednodes

    def reset_table(self):
        nodes = list(self.graph)
        for node in nodes:
            if node == self.startnode:
                self.table[node] = {'Cost': 0, 'Previous_node': ''}
            else:
                self.table[node] = {'Cost': self.INF, 'Previous_node': ''}




graph = Graph()

graph.set_startnode('A')
graph.addnode('A', {'B': 4, 'C': 2})
graph.addnode('B', {'A': 4, 'C': 1, 'D': 5})
graph.addnode('C', {'A': 2, 'B': 1, 'D': 8, 'E': 10})
graph.addnode('D', {'B': 5, 'C': 8, 'E': 2, 'Z': 6})
graph.addnode('E', {'C': 10, 'D': 2, 'Z': 5})
graph.addnode('Z', {'D': 6, 'E': 5})


def FindLinks():
    for

def CreateGraph(RootNode):
    Nodes = [] # parameter

    graph = Graph()
    graph.set_startnode(RootNode)







