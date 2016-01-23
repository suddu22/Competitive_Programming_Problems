def substring(s, slist):

    res = []
    for pattern in slist:
        res.append(kmp(s, pattern))

    final = [0] * len(slist)

    for j in range(len(res)):
        for i in range(len(res)):
            final[j] = min(res[i][j], res[i][j])

    return final



def computeTempArray(pattern):
    res = [0] * len(pattern)
    j = 0
    i = 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            res[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = res[j-1]
            else:
                res[i] = 0
                i += 1
    return res


def kmp(text, pattern):
    lps = computeTempArray(pattern)
    res = []
    i = 0
    j = 0
    start = -1

    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if start == -1:
                start = i
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == len(pattern):
            res.append(start-1)

            j = 0
            i -= 1
            start = -1

    return res

print substring("barfoothefoobarman", ["foo", "bar"])