"""
Given a stream of characters
(e.g. acacabcatghhellomvnsdb) and a list of words
(e.g. [ "aca","cat","hello","world"] )
find and display count of each and every word once the stream ends.
(Like : "aca" : 2 , "cat" : 1 , "hello" : 1 , "world" : 0 ).
[ Use LPS to make this counting online ].
"""


class WordsInStream:
    def __init__(self, words):
        self.words = words
        self.stream = []
        self.table = {}

        for w in words:
            self.table[w] = 0

    def addToSream(self, ch):
        if ch:
            self.stream.append(ch)

    def getWordsCount(self):
        stream = "".join(self.stream)

        for word in words:
            self._findPattern(word, stream)

        return self.table

    def _findPattern(self, pattern, text):
        lps = self._computeTempArray(pattern)
        n = len(text)
        m = len(pattern)

        i = 0
        j = 0

        while i < n and j < m:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

            if j == m:
                self.table[pattern] += 1
                i -= 1
                j = 0

    def _computeTempArray(self, pattern):
        n = len(pattern)
        lps = [0] * n

        j = 0
        i = 1

        while i < n:
            if pattern[i] == pattern[j]:
                lps[i] = j + 1
                j += 1
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


words = ["aca", "cat", "hello", "world"]
w = WordsInStream(words)
for ch in "acacabcatghhellomvnsdb":
    w.addToSream(ch)
print w.getWordsCount()
