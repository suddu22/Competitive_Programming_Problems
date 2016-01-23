
def prefix(A):
    res = []
    _prefix(A, 1, res)
    return res


def _prefix(words, i, res):
    table = {}
    for w in words:
        cur = w[:i]
        if cur in table:
            table[cur].append(w)
        else:
            table[cur] = [w]

    for (key, val) in table.items():
        if len(val) == 1:
            res.append(key)
        else:
            _prefix(val, i+1, res)

print prefix(['zebra', 'dog', 'duck', 'dove'])

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print vals[::2]