"""
Write a function get_hops_from(page1, page2) that will determine the number of hyperlinks that you would need to click on
to get from some page1 on the web to some other page2 on the web.
For example, if each page below links to the pages that are indented below it,
e.g. page 1 links to pages 2 and 5, and page 2 links to pages 3 and 4, and page 5 links to pages 3 and 7,
then the get_hops_from(page1, page7) should return 2 (2 hops),
since you have to hop once from page 1 to 5 and once more from page 5 to page 7.
page1 : distance == 0
page2 : distance == 1
page3 : distance == 2
page4 : distance == 2
page5 : distance == 2
page6 : distance == 2
page7 : distance == 2
Assume that an API is available to: * get_links(a_page) will return an array/list of all pages that a_page links to
https://www.glassdoor.com/Interview/Write-a-function-get-hops-from-page1-page2-that-will-determine-the-number-of-hyperlinks-that-you-would-need-to-click-on-t-QTN_739225.htm
"""

graph = {'1': ['2', '5'],
         '2': ['3', '4'],
         '3': [],
         '4': [],
         '5': ['3', '7'],
         '6': [],
         '7': []}

dfs_graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def get_links(a_page):
    return dfs_graph[a_page]


"""
BFS
- Uses Queue
- Shortest Path
- Explore the graph level by level
- O( V + E )
- Breath-First search provides us with the ability to return the same results as DFS
  but with the added guarantee to return the shortest-path first
"""


def get_hops_from(page1, page2):
    visited = set()
    distance = {}
    q = []

    q.insert(0, page1)
    distance[page1] = 0
    paths = []
    while len(q) > 0:
        current = q.pop()

        if current == page2:
            #print paths
            return distance[current]

        links = get_links(current)
        for nbr in links:
            if nbr not in visited:
                paths.append(nbr)
                visited.add(nbr)
                distance[nbr] = distance[current] + 1
                q.insert(0, nbr)
    return -1

print(get_hops_from('A', 'D'))

def get_hops_from_path(page1, page2):
    visited = set()
    distance = {}
    q = []

    q.insert(0, page1)
    distance[page1] = 0
    paths = []
    while len(q) > 0:
        current = q.pop()

        if current == page2:
            print paths
            return distance[current]

        links = get_links(current)
        for nbr in links:
            if nbr not in visited:
                paths.append(nbr)
                visited.add(nbr)
                distance[nbr] = distance[current] + 1
                q.insert(0, nbr)
    return -1

"""
DFS
- Uses Stack
- Explore every branch as deeply as possible
- O( V + E )
https://www.python.org/doc/essays/graphs/
"""

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newPath = find_path(graph, node, end, path)
            if newPath:
                return newPath
    return None


#print(find_path(dfs_graph, 'A', 'D'))


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            newPaths = find_all_paths(graph, node, end, path)
            for newPath in newPaths:
                paths.append(newPath)
    return paths


#print(find_all_paths(dfs_graph, 'A', 'D'))


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(shortest) > len(newpath):
                    shortest = newpath
    return shortest


#print(find_shortest_path(dfs_graph, 'A', 'D'))

def DFS_iterative(graph, start, end):
    visited = set()
    stack = [start]

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            stack.extend(graph[curr] - visited)
    return visited