"""
Find the top 500 most frequent words in the book. Print them as numbers, each in a line.

5000 the
4712 his
"""

import operator
import re
import heapq

def wordsFrequency_table():
    word_dict = {}
    book = open("input2.txt", 'r')
    for line in book:
        words = cleanStr(line)
        for word in [w for w in words if w != ""]:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    return word_dict

def cleanStr(w):
    wx = w.strip().lower()
    reg = re.split('\W+', wx)
    return reg

# O(n log n)
def wordsFrequency_sort(k):
    table = wordsFrequency_table()
    s_val = sorted(table.items(), key=operator.itemgetter(1), reverse=True)

    for (w, f) in s_val:
        if k == 0:
            break
        k -= 1
        print("%s: %d" % (w, f))

"""
T: O(n) => not sorted
S: O(1)
"""


def wordsFrequency_pivot(k):
    table = wordsFrequency_table()
    values = table.values()
    kth = findKth(values, k)
    for (w, f) in table.items():
        if k == 0:
            break
        if f >= kth:
            print("%s %d" % (w, f))
            k -= 1


def findKth(values, k):
    pivot = values[0]
    start = 0

    for i in range(len(values)):
        if values[i] > pivot:
            start += 1
            values[i], values[start] = values[start], values[i]

    values[0], values[start] = values[start], values[0]

    if start + 1 == k:
        return values[start]
    elif start + 1 > k:
        return findKth(values[:start], k)
    else:
        return findKth(values[start+1:], k)


"""
T: O(n)
S: O(n)
"""


def wordFrequency_heap(k):
    table = wordsFrequency_table()
    hlist = []
    for (w, f) in table.items():
        heapq.heappush(hlist, (-f, w))

    for i in range(k):
        curr = heapq.heappop(hlist)
        print("%s: %d" % (curr[1], -curr[0]))

k = 5
print "===heap==="
wordFrequency_heap(k)
print "===pivot==="
wordsFrequency_pivot(k)
print "===sort==="
wordsFrequency_sort(k)