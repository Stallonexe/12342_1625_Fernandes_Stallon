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
        self.targetnode = ""
        self.INF = 100

    def set_startnode(self, startnode):
        self.startnode = startnode

    def set_targetnode(self, targetnode):
        self.targetnode = targetnode

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
graph.set_targetnode('E')
graph.addnode('A', {'B': 4, 'C': 2})
graph.addnode('B', {'A': 4, 'C': 1, 'D': 5})
graph.addnode('C', {'A': 2, 'B': 1, 'D': 8, 'E': 10})
graph.addnode('D', {'B': 5, 'C': 8, 'E': 2, 'Z': 6})
graph.addnode('E', {'C': 10, 'D': 2, 'Z': 5})
graph.addnode('Z', {'D': 6, 'E': 5})







# Assign a temporary distance value to every node, starting with zero for the starting node and INF for the rest


PriorityQueue = PriorityQueue()

for node, columns in graph.table.items():
    PriorityQueue.enQueue(node, columns['Cost'])

while not PriorityQueue.isEmpty():
    vertex_u = PriorityQueue.deQueue()  # First item is popped
    u_key = list(vertex_u)[0]  # The key of the item
    u_value = vertex_u[u_key]  # The value of the item

    # Test2: Print current node and its value
    # print(f"Current Node: {u_key}, Value: {u_value}")

    # For each neighbour of the current node:
    for w_key, w_value in graph.graph[u_key].items():
        # Calculate the cost from the starting node to the neighbour
        cost = u_value + w_value

        # If the calculated cost is less than the current cost stored in Table:
        if cost < graph.table[w_key]['Cost']:
            # Update the cost and previous node in Table
            graph.table[w_key]['Cost'] = cost
            graph.table[w_key]['Previous_node'] = u_key

            # Update the priority queue with the new cost
            PriorityQueue.enQueue(w_key, cost)

    # Test3: Print the updated priority queue
    # print("Updated PriorityQueue:", PriorityQueue.queue)

# find the path
# Initialize a list to store the path

def traceback():
    path = []

    # Trace back the path from the destination node to the starting node
    current_node = graph.targetnode
    while current_node != '':
        path.insert(0, current_node)  # Insert the current node at the beginning of the path list
        current_node = graph.table[current_node]['Previous_node']  # Move to the previous node

    # Print the path
    print(f"Shortest Distance: {graph.table[graph.targetnode]['Cost']}")

    # test
    print("Shortest path from 'A' to 'Z':", ' -> '.join(path))

#print(graph.graph)
#print(graph.table)

traceback()