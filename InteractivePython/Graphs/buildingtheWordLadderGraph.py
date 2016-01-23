from pythonds.graphs.adjGraph import Graph, Vertex
from pythonds.basic.queue import Queue

"""
FOOL
POOL
POLL
POLE
PALE
SALE
SAGE
"""


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


#g = buildGraph("wordFile")
#bfs(g, g.getVertex("FOOL"))
#traverse(g.getVertex("SAGE"))

import string

def ladderLength(beginWord, endWord, wordList):

    dist = {}
    q = []

    done = set([beginWord])

    q.insert(0, beginWord)
    dist[beginWord] = 0

    if endWord not in wordList:
        wordList.add(endWord)

    while len(q) > 0:
        curr = q.pop()
        if curr == endWord:
            return dist[curr] + 1

        for i in range(len(curr)):
            for j in string.uppercase:
                candi = curr[:i] + j + curr[i+1:]
                if candi in wordList and candi not in done:
                    q.insert(0, candi)
                    done.add(candi)
                    dist[candi] = dist[curr] + 1

    return 0

st = set(["FOOL", "POOL", "POLL", "POLE", "PALE", "SALE", "SAGE"])
print ladderLength("FOOL", "SAGE", st)

def findLadders(beginWord, endWord, wordList):

    wordList.add(endWord)
    wordList.add(beginWord)
    dist = {}
    q = []

    trace = dict([(w, []) for w in wordList])

    done = set([beginWord])

    q.insert(0, beginWord)
    dist[beginWord] = 0

    while len(q) > 0:
        curr = q.pop()

        for i in range(len(curr)):
            for j in string.uppercase:
                candi = curr[:i] + j + curr[i+1:]
                if candi in wordList and candi not in done:
                    q.insert(0, candi)
                    done.add(candi)
                    dist[candi] = dist[curr] + 1
                    trace[candi].append(curr)
    res = []
    findLaddersTraverse(res, trace, [], endWord)

    return res


def findLaddersTraverse(res, trace, path, word):
    if not trace[word]:
        res.append([word] + path)
    else:
        for prev in trace[word]:
            findLaddersTraverse(res, trace, [word] + path, prev)

st = set(["FOOL", "POOL", "POLL", "POLE", "PALE", "SALE", "SAGE"])
print findLadders("FOOL", "SAGE", st)