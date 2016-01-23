"""  Write an algorithm for finding if a word is partial anagram of another word:
For example : booking <- bing true What is the complexity of the written algoritm.  """


def doit(s, subs):
    h = {}
    for c in s:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1
    for c in subs:
        if c not in h or h[c] == 0:
            return False
        h[c] -= 1
    return True


def partialAnagram(word, target):

    char_dict = {}

    for c in word:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    for c in target:
        if c not in char_dict or char_dict[c] == 0:
            return False
        else:
            char_dict[c] -= 1

    return True

print(partialAnagram("booking", "bing"))
