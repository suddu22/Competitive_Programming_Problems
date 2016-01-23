def anagramCheck(s1, s2):

    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}

    for s in s1:
        if s in d1:
            d1[s] += 1
        else:
            d1[s] = 1

    for s in s2:
        if s in d2:
            d2[s] += 1
        else:
            d2[s] = 1

    for s in s1:
        if d1[s] != d2[s]:
            return False

    return True

def anagramCheck2(s1, s2):

    if len(s1) != len(s2):
        return False

    d1 = {}

    for s in s1:
        if s in d1:
            d1[s] += 1
        else:
            d1[s] = 1

    for s in s2:
        if s not in d1:
            return False
        elif d1[s] <= 0:
            return False
        else:
            d1[s] -= 1

    for c in d1:
        if d1[c] > 0:
            return False

    return True

print(anagramCheck2('applea','pleeap'))