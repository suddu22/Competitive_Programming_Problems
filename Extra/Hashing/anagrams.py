
def anagrams(A):

    ana_dict = {}
    res = []
    for i in range(len(A)):
        word = A[i]
        sword = "".join(sorted(word)).strip()
        if sword in ana_dict:
            ana_dict[sword].append(i+1)
        else:
            ana_dict[sword] = [i+1]

    for k in ana_dict:
        res.append(ana_dict[k])

    return res


print anagrams(['cat', 'dog', 'god', 'tca'])