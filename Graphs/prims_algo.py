'''
Prim's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which

form a tree that includes every vertex
has the minimum sum of weights among all the trees that can be formed from the graph

'''
#not implemented fully

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def prims_algo(self, start_vertex):
        pass

    def display(self):
        for i in self.graph:
            pass
        pass

    def get_min(self, input):
        min = 99
        for i in input:
            if i != 0 and i < min:
                min = i
        return min
                


if __name__ == "__main__":
    graph = [ 
                [0, 2, 0, 6, 0], 
                [2, 0, 3, 8, 5], 
                [0, 3, 0, 0, 7], 
                [6, 8, 0, 0, 9], 
                [0, 5, 7, 9, 0]
            ]
    Obj = Graph(graph)
    Obj.display()
    #print("min : ", Obj.get_min([0, 2, 0, 6, 0]))
    #Obj.prims_algo(0)



