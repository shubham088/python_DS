'''
Implementation for Kuruskal's Algorithm
'''

class Edges:
    def __init__(self, src, dest, weight):
        self.source = src
        self.destination = dest
        self.weight = weight
        self.edge = (src, dest)


class KuruskalAlgo:
    def __init__(self, graph):
        self.Graph = graph
        self.visited_list = []
        self.input_edges = []
        self.finalMST = [[0 for i in range(self.getNumberofNodes())] for j in range(self.getNumberofNodes())]

    def getNumberofNodes(self):
        return len(self.Graph)

    def order_edges(self):
        for i in range(0, len(self.input_edges)):
            for j in range(0, len(self.input_edges)-1):
                if self.input_edges[j].weight > self.input_edges[j+1].weight:
                    self.input_edges[j], self.input_edges[j+1] = self.input_edges[j+1], self.input_edges[j]


    #storing all the edges in the given graph
    def store_all_edges(self):
        for u in range(0, self.getNumberofNodes()):
            for v in range(0, self.getNumberofNodes()):
                duplicate = 0
                if self.Graph[u][v] != 0 and self.Graph[u][v] != 999:
                    obj = Edges(v,u,self.Graph[u][v])
                    for i in range(0, len(self.input_edges)):
                        if obj.edge == self.input_edges[i].edge:
                            duplicate = 1
                        
                    if duplicate == 0:
                        self.input_edges.append(Edges(u,v,self.Graph[u][v]))

        
        print("stored all edges into input edge list..")
        self.order_edges()

    def kuruskal_algorithm(self):
        # no. of edges in mst is always vertices - 1
        count = 0
        edges_mst = self.getNumberofNodes()-1
        #while count < edges_mst:
        print("edges in mST : ", edges_mst)
        for i in range(0, len(self.input_edges)):
            if count == edges_mst:
                break
            src = self.input_edges[i].source
            dest = self.input_edges[i].destination
            cost = self.input_edges[i].weight
            self.finalMST[src][dest] = cost
            self.analyzeMST(src)
            if len(self.visited_list) == len(set(self.visited_list)): # no duplication
                #print("{}-{} added in MSt".format(src, dest))
                count = count+1
                self.visited_list.clear()
            else:
                self.finalMST[src][dest] = 0
                self.visited_list.clear()

                

    # dfs implementation to check if cycle presents in graph        
    def analyzeMST(self, source):
        
        self.visited_list.append(source)

        for v in range(0, len(self.finalMST)):
            if self.finalMST[source][v] != 0  :
                self.analyzeMST(v)

            
        
    def display_sorted_array(self):
        print("sorted edges...")
        for i in range(0, len(self.input_edges)):
            print(self.input_edges[i].edge)  

    def display_mst(self):
        for u in range(0,len(self.finalMST)):
            for v in range(0, len(self.finalMST)):
                if self.finalMST[u][v]!=0:
                    print("{}->{} = {}".format(u,v, self.finalMST[u][v]))

    


sample_graph = [
    [999, 5,3,999,999,7],
    [5,999,6,2,4,999],
    [3,6,999,3,999,8],
    [999,2,3,999,2,999],
    [999,4,999,2,999,999],
    [7,999,8,999,999,999]
]

g = KuruskalAlgo(sample_graph)
g.store_all_edges()
g.display_sorted_array()
g.kuruskal_algorithm()
g.display_mst()

