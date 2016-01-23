graph = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]


def word_search(graph, word):
    if not graph:
        return False
    if not word:
        return False

    rows = len(graph)
    cols = len(graph[0])

    for i in range(rows):
        for j in range(cols):
            if dfs(graph, word, i, j, 0):
                return True
    return False


def dfs(graph, word, i, j, k):
    rows = len(graph)
    cols = len(graph[0])

    if i < 0 or j < 0 or i >= rows or j >= cols:
        return False

    if word[k] == graph[i][j]:
        temp = graph[i][j]
        graph[i][j] = "#"

        if k == len(word) - 1:
            return True

        if dfs(graph, word, i + 1, j, k + 1) \
                or dfs(graph, word, i - 1, j, k + 1) \
                or dfs(graph, word, i, j + 1, k + 1) \
                or dfs(graph, word, i, j - 1, k + 1):
            return True

        graph[i][j] = temp

    return False


#print word_search(graph, "ABCCED")
print word_search([["a"]], "a")
