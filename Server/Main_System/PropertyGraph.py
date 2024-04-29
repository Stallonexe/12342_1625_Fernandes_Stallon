from Properties import Property



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

print(graph.graph)

