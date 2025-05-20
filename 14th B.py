class Graph:
    def __init__(self, vertices):
        self.V = vertices

    
    def printSolution(self, reach):
        print("Transitive Closure of the given graph:")
        for i in range(self.V):
            for j in range(self.V):
                print("%3d" % (1 if i == j else reach[i][j]), end=" ")
            print()

    
    def transitiveClosure(self, graph):
        reach = [row[:] for row in graph]
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        self.printSolution(reach)


g = Graph(4)
graph = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]
g.transitiveClosure(graph)
