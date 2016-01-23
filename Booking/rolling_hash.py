"""
Given a stream of characters (e.g. acacabcatghhellomvnsdb) and a list of words (e.g. [ "aca","cat","hello","world"] )
find and display count of each and every word once the stream ends.
(Like : "aca" : 2 , "cat" : 1 , "hello" : 1 , "world" : 0 ).
[ Use LPS to make this counting online ].
"""


"""
T: O(mn)
"""
def wordCountStream(stream, wlist):
    res = {}
    for w in wlist:
        start = 0
        end = len(stream) - len(w)
        res[w] = 0
        while start <= end:
            window = stream[start:start+len(w)]
            if window == w:
                res[w] += 1
            start += 1

    return res

wlist = ["aca", "cat", "hello", "world"]
print wordCountStream("acacabcatghhellomvnsdb", wlist)

"""
T: O(m+n)
S: O(n)
"""
def wordCountStream_KMP(text, patterns):

    res = {}
    for pattern in patterns:
        cnt = kmp(text, pattern)
        res[pattern] = cnt

    return res


def computeTempArray(pattern):
    lps = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[j] == pattern[i]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern):
    cnt = 0
    lps = computeTempArray(pattern)
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == len(pattern):
            cnt += 1
            i -= 1
            j = 0

    return cnt


wlist = ["aca", "cat", "hello", "world"]
print wordCountStream_KMP("acacabcatghhellomvnsdbaaccaaccaa", wlist)

print [0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 4]
print computeTempArray("acacabacacabacacac")