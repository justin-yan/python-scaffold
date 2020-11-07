from typing import List, Set, Callable, Dict
from collections import defaultdict

class Vertex:
    def __init__(self):
        self.id = -1
        self.degree = 0
        self.neighbors = set()

    def setId(self, vid: int):
        self.id = vid

    def getId(self):
        return self.id

    def incrementDegree(self):
        self.degree += 1

    def getDegree(self):
        return self.degree

    def addNeighbor(self, vertex: int):
        self.neighbors.add(vertex)

    def hasNeighbor(self, vertex: int):
        return vertex in self.neighbors

    def getNeighbors(self):
        return self.neighbors

class Graph:
    """
    Graph: unique, undirected edges, no weights on vertex or edges.
    """

    def __init__(self, numVertices: int, edgeList: List[List[int]]):
        self.nodeIndex: Dict[int, Vertex] = defaultdict(Vertex)

        for vertOrd in range(numVertices):
            self.nodeIndex[vertOrd + 1].setId(vertOrd + 1)

        for edge in edgeList:
            v1 = self.nodeIndex[edge[0]]
            v1.incrementDegree()
            v1.addNeighbor(edge[1])
            v2 = self.nodeIndex[edge[1]]
            v2.incrementDegree()
            v2.addNeighbor(edge[0])

    def getVertex(self, vertex: int) -> Vertex:
        return self.nodeIndex[vertex]

    def isEdge(self, vertex1: int, vertex2: int) -> bool:
        return self.nodeIndex[vertex1].hasNeighbor(vertex2)

    def vertexList(self,
                   sort_by: Callable[[Vertex], int] = lambda v: v.getId(),
                   descending = True,
                   filter_by: Callable[[Vertex], bool] = lambda v: True) -> List[int]:
        return [v[0] for v in sorted(self.nodeIndex.items(), key=lambda pair: sort_by(pair[1]), reverse=descending) if filter_by(v[1])]

    # TODO: Shortest path between two vertices
    # TODO: Add support for weights on vertices


if __name__ == '__main__':
    g = Graph(7, [[1,2],[1,3],[1,4]])
    print(g.isEdge(1,2))
    print(g.isEdge(1,6))
    print(g.vertexList(sort_by=lambda v: v.getDegree(), descending=False, filter_by=lambda v: v.getDegree() > 0))
    print(g.vertexList(sort_by=lambda v: v.getId(), descending=True, filter_by=lambda v: v.getDegree() > 0))

    print(g.getVertex(1).getDegree())
    print(g.getVertex(3).getDegree())

    print(g.getVertex(1).getNeighbors())