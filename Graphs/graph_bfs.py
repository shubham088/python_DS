class BFSAlgo:
    def __init__(self, graph=None):
        self.visited = list()
        self.queue = list()
        if graph is None:
            self.graph = None
        else:
            self.graph = graph

    def bfs_alogorithm(self, start_vertex):
        # mark the vertex as visited
        self.visited.append(start_vertex)
        #place the vertex in queue
        self.queue.append(start_vertex)
        #now iterate through the neighbours for start_vertex
        
        while self.queue:
            current_vertex = self.queue.pop(0)
            for neighbour in self.graph[current_vertex]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)

    
    def display_result_bfs(self):
        print("BFS result is  : ", self.visited)

    def display_graph(self):
        for keys in self.graph.keys():
            if len(self.graph[keys]) == 0:
                print(keys)
            for vertex in self.graph[keys]:
                print("{}------>{}".format(keys, vertex))

            

    

if __name__ == "__main__":
    graph_elements = {
                    'A' : ['B','C'],
                    'B' : ['D', 'E'],
                    'C' : ['F'],
                    'D' : [],
                    'E' : ['F'],
                    'F' : []
                    }

    graph = BFSAlgo(graph_elements)
    graph.display_graph()
    graph.bfs_alogorithm('A')
    print('bfs algorithm starting from vertex \'a\' ')
    graph.display_result_bfs()


