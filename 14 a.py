from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to):
        self.graph[frm].append(to)
        if not self.directed:
            self.graph[to].append(frm)
        else:
            # Ensure all nodes are in the graph
            if to not in self.graph:
                self.graph[to] = self.graph[to]

    def topoSortvisit(self, s, visited, sortlist):
        visited[s] = True
        for i in self.graph[s]:
            if not visited[i]:
                self.topoSortvisit(i, visited, sortlist)
        sortlist.insert(0, s)

    def topoSort(self):
        visited = {i: False for i in self.graph}
        sortlist = []
        for v in self.graph:
            if not visited[v]:
                self.topoSortvisit(v, visited, sortlist)
        print(sortlist)

# Main block
if __name__ == '__main__':
    g = Graph(directed=True)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 6)
    g.addEdge(4, 6)

    print("Topological Sort:")
    g.topoSort()
