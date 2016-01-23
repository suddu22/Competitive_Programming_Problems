"""
Write an algorithm for finding if a word is partial anagram of another word:
For example : booking <- bing true
What is the complexity of the written algorithm.
"""


def partial_anagram(w1, w2):
    if not w1 or not w2:
        return False

    table = {}
    for ch in w1:
        if ch in table:
            table[ch] += 1
        else:
            table[ch] = 1

    for ch in w2:
        if ch in table and table[ch] > 0:
            table[ch] -= 1
        else:
            return False
    return True

print partial_anagram("booking", "bing")