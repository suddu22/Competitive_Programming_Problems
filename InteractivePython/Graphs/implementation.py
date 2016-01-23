
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight):
        self.connectedTo[nbr] = weight

    def getId(self):
        return self.id

    def geWeight(self, nbr):
        return self.connectedTo[nbr]

    def getConnections(self):
        return self.connectedTo.keys()

    def __str__(self):
        return str(self.id) + " is connected to " + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertex = 0

    def __contains__(self, item):
        return item in self.vertexList

    def addEdge(self, t, f, cost=0):
        if t not in self.vertexList:
            tn = self.addVertex(t)
        if f not in self.vertexList:
            fn = self.addVertex(f)
        return self.vertexList[t].addNeighbour(self.vertexList[f], cost)


    def addVertex(self, key):
        self.numVertex += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def getVertexes(self):
        return self.vertexList

    def __iter__(self):
        return iter(self.vertexList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
    g.vertexList
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
