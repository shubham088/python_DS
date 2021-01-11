'''
Graphs Data Structure : A graph is a pictorial representation of 
a set of objects where some pairs of objects are connected by links.
 The interconnected objects are represented by points termed as vertices, 
 and the links that connect the vertices are called edges. 


      a-----------------b
      |                 |
      |                 |
      |                 |
      |                 |
      c-----------------d---------------e

'''

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

#Get the edges of the graph
    def getEdges(self):
        edges = list()
        for keys in self.gdict.keys():
            #print('key : ', keys)
            #print("{}------>{}".format(keys, self.gdict[keys]))
            for vertices in self.gdict[keys]:
             #   print('vertices : ', vertices)
                if  str(vertices)+str(keys) not in edges:
                    edges.append(str(keys)+str(vertices))
        return edges


# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.getVertices())

print("printing edges.....")
print(g.getEdges())