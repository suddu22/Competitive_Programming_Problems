"""
We've got a book.txt that contains text of a book written with English alphabet.

Transform the words in this book into numbers. For simplicity, escape all non English alphabet characters.
Print the output on STDOUT.

Example IN:

This is a sample
for this problem.
It is short,
compared to a book.

Example OUT:

1 2 3 4
5 1 6
7 2 8
9 10 3 11

Note: no need to preserve newlines!
"""

import re
import random


def wordsToNumbers():
    word_dict = {}
    count = 1
    book = open("input1", 'r')
    for line in book:
        words = cleanStr(line)
        for word in words:
            if word == "":
                continue
            if word not in word_dict:
                word_dict[word] = count
                count += 1
            print word_dict[word],
        print

    return word_dict


def cleanStr(w):
    wx = w.strip().lower()
    reg = re.split('\W+', wx)
    return reg

    # return "".join([ch for ch in w if ch not in string.punctuation]).split()


wordsToNumbers()

"""
Output the words found in a stream of characters.
- Input: Dictionary<string>, Stream
- Output: Dictionary containing words and their occurrences.
- Complexity, best case, worst case
"""

'''
Find the top 500 most frequent words in the book. Print them as numbers, each in a line.

5000 the
4712 his
'''

import operator


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


# O(n log n)
def wordsFrequency(k):
    table = wordsFrequency_table()
    s_val = sorted(table.items(), key=operator.itemgetter(1), reverse=True)

    for (w, f) in s_val:
        if k == 0:
            break
        k -= 1
        print("%s: %d" % (w, f))
wordsFrequency(5)
print


# O(n)
def wordsFrequency_better(k):
    table = wordsFrequency_table()
    values = table.values()
    kth = kth_largest(values, 0, len(values) - 1, len(values) - k)
    for (w, f) in table.items():
        if k == 0:
            break
        if f >= kth:
            print("%s %d" % (w, f))
            k -= 1

def partition1(arr, left, right, pivotIndex):
    arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]
    pivot = arr[right]
    swapIndex = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            swapIndex += 1
    arr[right], arr[swapIndex] = arr[swapIndex], arr[right]
    return swapIndex


def kth_largest(alist, left, right, k):
    if not 1 <= k <= len(alist):
        return
    if left == right:
        return alist[left]

    while True:
        ran = random.randint(left, right)
        ppoint = partition1(alist, left, right, ran)
        if ppoint + 1 == k:
            return alist[ppoint]
        elif ppoint + 1 > k:
            return kth_largest(alist, left, ppoint - 1, k)
        else:
            return kth_largest(alist, ppoint + 1, right, k)

            # wordsFrequency_better(5)
