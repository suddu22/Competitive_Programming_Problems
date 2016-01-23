# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
#
# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#

# BFS

def findLadders(start, end, dictList):
    dictList.add(start)
    dictList.add(end)

    result, cur, visited, found = [], [start], set([start]), False
    trace = dict([(w, []) for w in dictList])

    while cur and not found:
        for word in cur:
            visited.add(word)

        next = set()
        for word in cur:
            for i in xrange(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + j + word[i + 1:]
                    if candidate not in visited and candidate in dictList:
                        if candidate == end:
                            found = True
                        next.add(candidate)
                        trace[candidate].append(word)
        cur = next

    if found:
        backtrack(result, trace, [], end)

    return result


def backtrack(result, trace, path, word):
    if not trace[word]:
        result.append([word] + path)
    else:
        for prev in trace[word]:
            backtrack(result, trace, [word] + path, prev)


print findLadders("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
