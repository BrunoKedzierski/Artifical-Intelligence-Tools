class Node:
    def __init__(self, value):
        self.neighbors = []
        self.value = value
    def add_neighbors(self, neighbor):
        self.neighbors.append(neighbor)

class graph:
    def __init__(self):
        self.nodes = []
    def add_node(self, node):
        self.nodes.append(node)