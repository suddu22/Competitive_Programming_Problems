from pythonds.basic.deque import Deque


def palindromChecker(word):
    de = Deque()
    for w in word:
        de.addRear(w)

    stillEqual = True
    while de.size() > 1 and stillEqual:
        f = de.removeFront()
        r = de.removeRear()
        if f != r:
            return False

    return stillEqual

print(palindromChecker("lsdkjfskf"))
print(palindromChecker("radar"))