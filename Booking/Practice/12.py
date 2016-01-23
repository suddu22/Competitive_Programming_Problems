"""
Find the top 500 most frequent words in the book. Print them as numbers, each in a line.

5000 the
4712 his
"""
import re
def wordsFrequency_table(file_name):
    word_dict = {}
    book = open(file_name, 'r')
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

"""
T: O(n) => not sorted
S: O(1)
"""

def wordsFrequency_pivot(file_name, k):
    table = wordsFrequency_table(file_name)
    values = table.values()
    res = []

    kth = wordsFrequency_kth(values, k)

    for (w, f) in table.items():
        if f >= kth:
            res.append([f, w])
            print("%s %d" % (w, f))
    return res

def wordsFrequency_kth(values, k):
    pivot = values[0]
    index = 0

    for i in range(len(values)):
        if values[i] > pivot:
            index += 1
            values[i], values[index] = values[index], values[i]
    values[0], values[index] = values[index], values[0]

    if index + 1 == k:
        return pivot
    elif index + 1 > k:
        return wordsFrequency_kth(values[:index], k)
    else:
        return wordsFrequency_kth(values[index+1:], k - index - 1)

wordsFrequency_pivot("12", 3)

"""
T: O(n)
S: O(n)
"""
import heapq
def wordsFrequency_heap(file_name, k):
    table = wordsFrequency_table(file_name)
    hlist = []
    for (w, f) in table.items():
        heapq.heappush(hlist, (-f, w))

    for i in range(k):
        curr = heapq.heappop(hlist)
        print("%s: %d" % (curr[1], -curr[0]))

print 
wordsFrequency_heap("12", 3)