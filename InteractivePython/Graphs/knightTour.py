from pythonds.graphs.adjGraph import Graph, Vertex

# exponential algorithm of size O(k^N), where N is the number of squares on the chess board, and k is a small constant.

def knightGraph(bdSize):
    g = Graph()
    for col in range(bdSize):
        for row in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            moves = getLegalMoves(row, col, bdSize)
            for move in moves:
                nid = posToNodeId(move[0], move[1], bdSize)
                g.addEdge(nodeId, nid)
    return g


def posToNodeId(row, column, bdSize):
    return (row * bdSize) + column


def getLegalMoves(x, y, bdSize):
    moves = []
    offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
               (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for i in offsets:
        newX = x + i[0]
        newY = y + i[1]
        if isLegalMove(newX, bdSize) and isLegalMove(newY, bdSize):
            moves.append((newX, newY))
    return moves


def isLegalMove(p, bdSize):
    if p >= 0 and p < bdSize:
        return True
    return False


# DFS
def knightTour(n, path, v,limit):
    v.setColor('gary')
    path.append(v)

    if n < limit:
        #nbrs = list(v.getConnections())
        nbrs = list(orderByAvail(v))
        i = 0
        done = False

        while i < len(nbrs) and not done:
            if nbrs[i].getColor == 'white':
                done = knightTour(n+1, path, nbrs[i], limit)
            i += 1

        if not done:
            path.pop()
            v.setColor('white')
    else:
        done = True

    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[1])
    return [y[1] for y in resList]
