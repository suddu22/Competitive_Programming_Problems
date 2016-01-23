"""
Implement a function all_anagram_groups() that, given many input strings,
will identify and group words that are anagrams of each other.
An anagram is word that is just a re-arrangement of the characters of another word,
like "reap" and "pear" and "a per" (whitespace is ignored). But "pear" and "rep" are not,
since "rep" does not have an "a".
Also, "the" and "thee" are not anagrams, because "the" only has one "e".
Given this example input: [ "pear","dirty room","amleth","reap","tinsel","hamlet","dormitory","listen","silent" ]
The output should be an array-of-arrays (or list-of-lists)
[ ["pear","reap"], ["dirty room","dormitory"], ["amleth","hamlet"], ["tinsel","listen","silent"] ]
https://www.glassdoor.com/Interview/Implement-a-function-all-anagram-groups-that-given-many-input-strings-will-identify-and-group-words-that-are-anagrams-o-QTN_739224.htm
"""
"""
http://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/
"""


class word():
    def __init__(self, string, index):
        self.string = string
        self.index = index


"""
Sorting array of words takes NLogN comparisons.
A comparison may take maximum O(M) time.
So time to sort array of words will be O(MNLogN)
"""


def printAnagramsTogether(words):
    wordList = []
    n = len(words)
    for w in range(n):
        wordList.append(word(words[w], w))

    for w in range(n):
        wordList[w].string = "".join(sorted(wordList[w].string))
    wordList = sorted(wordList, key=lambda x: x.string)

    for w in wordList:
        print words[w.index]


# wordArr = ["cat", "dog", "tac", "god", "act"]
# result = "cat tac act dog god"

wordArr = ["pear", "dirty room", "amleth", "reap", "tinsel", "hamlet", "dormitory", "listen", "silent"]


# result = [ ["pear","reap"], ["dirty room","dormitory"], ["amleth","hamlet"], ["tinsel","listen","silent"] ]

def all_anagram_groups(words):
    dict = {}
    group = []

    for w in words:
        ws = "".join(sorted(w)).strip()
        if ws not in dict:
            dict[ws] = [w]
        else:
            dict[ws].append(w)

    for k in dict:
        group.append(dict[k])

    print group


all_anagram_groups(wordArr)


def isPalindrom(word):
    n = len(word)
    for i in range(n / 2):
        if word[i] is not word[n - i - 1]:
            return False
    return True


# print(isAnagram("ahjmxmjha", 3, 5))
allP = []


def allPalindromic_rec(currentP, start, n, word):
    if start >= n:
        allP.append(currentP[:])
        return

    for i in range(start, n):
        if isPalindrom(word, start, i):
            currentP.append(word[start:i + 1])
            allPalindromic_rec(currentP, i + 1, n, word)
            currentP.pop()


def allPalindromic(word):
    n = len(word)
    start = 0
    currentP = []
    allPalindromic_rec(currentP, start, n, word)

    for p in allP:
        print p,


def isPalindrom(word, start, end):
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

# print(allPalindromic("nitin"))
