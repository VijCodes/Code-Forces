from collections import defaultdict
class Node():
    def __init__(self,val = None):
        self.connections = defaultdict(lambda: defaultdict(Node))
        self.val = val
class DELG():
    def __init__(self):
        self.nodes = defaultdict(Node)
    def addNode(self,value):
        self.nodes[value] = Node(value)
    def addConnection(self,start,end,label):
        if start not in self.nodes:
            print(f'Node:{start} is not found in the graph. Unable to add connection {start}-->-{label}-->-{end}')
            return 
        if end not in self.nodes:
            self.addNode(end)
        self.nodes[start].connections[label][end] = self.nodes[end]
       

NewGraph = DELG()
NewGraph.addNode('Hyderabad')
NewGraph.addConnection('Hyderabad','AP','capital')



    

