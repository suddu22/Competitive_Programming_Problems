"""
There's a very simple compression algorithm that takes subsequent characters and just emits how often they were seen.

Example:
abababaabbbaaaaa

"""

def compress(string):
    prev = None
    cons = 1
    compressed = ''
    for i in string:
        if prev:
            if prev == i:
                cons += 1
            else:
                compressed += prev+str(cons)
                cons = 1
        prev = i
    compressed += prev+str(cons)

    return compressed

print compress("aaaaaaaabcaaa")

def compressString(letters):

    res = []
    prev = letters[0]
    count = 1

    for i in range(1, len(letters)):
        if prev == letters[i]:
            count += 1
        else:
            res.append(prev)
            res.append(str(count))
            prev = letters[i]
            count = 1

    res.append(prev)
    res.append(str(count))

    return "".join(res)

print compressString("aaaaaaaabcaaa")