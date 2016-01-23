"""
Given a list/array of names(String)
sort them such that each name is followed by a name which starts with the last character of the previous name.
# input
[
Luis
Hector
Selena
Emmanuel
Amish
]

# output:
[
Emmanuel
Luis
Selena
Amish
Hector
]

"""
"""
L: LUIS, H: HECTOR, S: SELENA, E: EMMANUEL, A: AMISH
L: EMMANUEL, S: LUIS, A:SELENA, H: AMISH, R: HECTOR
"""

def sort_start_end(names):
    if not names:
        return []

    begins = {}
    ends = {}
    res = []

    for name in names:
        begins[name[0]] = name
        ends[name[-1]] = name

    start = name[0]
    for (k, v) in begins.items():
        if k not in ends:
            start = v

    res.append(start)
    current = start

    while current:
        letter = current[-1]
        if letter in begins:
            res.append(begins[letter])
            current = begins[letter]
        else:
            current = None

    return res

print sort_start_end(['RAHUK', 'KALLI', 'LUIS', 'HECTOR', 'SELENA', 'EMMANUEL', 'ANISH'])