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
def sort(input):
    firstLetter = {}
    lastLetter = {}
    first = None
    output = []
    for value in input:
        firstLetter[value[0]] = value
        lastLetter[value[-1]] = value
    for value in input:
        cc = value[0]
        if value[0] in lastLetter:
            continue
        else:
            first = value
            break;
    if not first:
        first = input[0]
    output.append(first)
    del firstLetter[first[0]]
    next = first[-1]
    for value in firstLetter:
        output.append(firstLetter[next])
        next = firstLetter[next][-1]
    return output

print sort(['RAHUK', 'KALLI', 'LUIS', 'HECTOR', 'SELENA', 'EMMANUEL', 'ANISH'])
print sort(['RAHUK', 'KALLI', 'LUIS', 'HECTOR', 'SELENA', 'ANISH'])


def lastIsFirst(words):

    first = {}
    last = {}
    res = []

    for word in words:
        first[word[0]] = word
        last[word[-1]] = word

    start = words[0]

    for word in words:
        if word[0] not in last:
            start = word

    res.append(start)
    while start:
        letter = start[-1]
        if letter in first:
            curr = first[letter]
            res.append(curr)
            start = curr
        else:
            start = None

    return res

print lastIsFirst(['RAHUK', 'KALLI', 'LUIS', 'HECTOR', 'SELENA', 'EMMANUEL', 'ANISH'])