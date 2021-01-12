class DFSAlgo:
    def __init__(self, graph=None):
        self.visited = list()
        if graph is None:
            self.graph = None
        else:
            self.graph = graph

    def dfs_alogorithm(self, vertex):
       #mark the vertex as visited
       self.visited.append(vertex)
       if len(self.graph[vertex]):
           for neighbour in self.graph[vertex]:
               if neighbour not in self.visited:
                   self.dfs_alogorithm(neighbour)
    
    def display_result_dfs(self):
        print("DFS result is  : ", self.visited)

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

    graph = DFSAlgo(graph_elements)
    graph.display_graph()
    graph.dfs_alogorithm('A')
    print('dfs algorithm starting from vertex \'a\' ')
    graph.display_result_dfs()


