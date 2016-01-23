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

"""
BFS
- Uses Queue
- Shortest Path
- Explore the graph level by level
- O( V + E )
- Breath-First search provides us with the ability to return the same results as DFS
  but with the added guarantee to return the shortest-path first
"""

graph = {'1': ['2', '5'],
         '2': ['3', '4'],
         '3': [],
         '4': [],
         '5': ['3', '7'],
         '6': [],
         '7': []}

def get_links(a_page):
    return graph[a_page]

def get_hops_from(page1, page2):
    if not page1 and not page2:
        return None

    visited = set()
    distance = {}
    q = []

    q.insert(0, page1)
    distance[page1] = 0
    while len(q) > 0:
        pop = q.pop()
        if pop == page2:
            return distance[pop]

        links = get_links(pop)
        for link in links:
            if link not in visited:
                q.insert(0, link)
                distance[link] = distance[pop] + 1
                visited.add(link)
    return -1

print get_hops_from('1','7')

"""
DFS
- Uses Stack
- Explore every branch as deeply as possible
- O( V + E )
https://www.python.org/doc/essays/graphs/
"""
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_all_paths(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    res = []

    for node in graph[start]:
        if node not in path:
            new_path = find_all_paths(graph, node, end, path)
            for p in new_path:
                res.append(p)
    return res

print(find_all_paths(graph, 'A', 'D'))