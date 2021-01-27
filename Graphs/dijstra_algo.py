

class DijkstraAlgo:
    def __init__(self, graph):
        self.Graph = graph
        self.visited = list()
        self.source = None
    
    def setSourceNode(self, node):
        self.source = node

    def findNodes(self):
        return len(self.Graph)-1    #because we are using extra row of zero's

    def initializeVistedNodes(self):
        num = self.findNodes()
        print("no of nodes : ", num)
        for i in range(0, num+1):    #because of extra zero's
            self.visited.append(0)

        #print("visited list at very begining : ", self.visited)

    def applyDijkstraAlgo(self, currentNode=None):
        if currentNode is None:
            currentNode = self.source
        #print("current node : ", currentNode)
         #mark the current node as visited so that again we can't visit the same node
        self.visited[currentNode] = 1
        #print("current status for visited node : ", self.visited)

       
        count = 0 
        for nodes_visited in self.visited:
            if nodes_visited == 1:
                count += 1
        if count == self.findNodes():
            print("algorithm is completed")
            return 

        # this list defines all the neighbours
        neighbours = self.Graph[currentNode]
        #print("neighbours for node {} => {}".format(currentNode, neighbours))
        #find minimum in this list and node should be unvisited
        minNode = 0
        minCost = 99
        for neighbour in range(1, len(neighbours)):
            if self.visited[neighbour] == 0 and self.Graph[currentNode][neighbour] < minCost:
                minNode = neighbour
                minCost = self.Graph[currentNode][neighbour]


        if self.Graph[self.source][minNode] > self.Graph[self.source][currentNode]+self.Graph[currentNode][minNode]:
            ## now update the graph with min values
            self.Graph[self.source][minNode] = self.Graph[self.source][currentNode]+self.Graph[currentNode][minNode]
        
        self.applyDijkstraAlgo(minNode)


    def displayShortestPathFromSource(self):
        final_result = self.Graph[self.source]

        for i in range(1, len(final_result)):
            print("{} -> {} = {}".format(self.source, i, final_result[i]))




sample_graph = [
[0,0,0,0,0,0,0],                 #added extra row, column so that we can compute using index 1
[0,0,4,2,999,999,999],
[0,4,0,999,999,3,999],
[0,2,999,0,2,999,4],
[0,999,999,2,0,3,1],
[0,999,3,999,3,0,1],
[0,999,999,4,1,1,999]
]

g = DijkstraAlgo(sample_graph)

g.setSourceNode(1)
g.initializeVistedNodes()

g.applyDijkstraAlgo()

g.displayShortestPathFromSource()



            








