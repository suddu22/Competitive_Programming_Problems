"""
Implement a function all_anagram_groups() that, given many input strings,
will identify and group words that are anagrams of each other.
An anagram is word that is just a re-arrangement of the characters of another word,
like "reap" and "pear" and "a per" (whitespace is ignored). But "pear" and "rep" are not,
since "rep" does not have an "a".
Also, "the" and "thee" are not anagrams, because "the" only has one "e".
Given this example input:
[ "pear","dirty room","amleth","reap","tinsel","hamlet","dormitory","listen","silent" ]
The output should be an array-of-arrays (or list-of-lists)
[ ["pear","reap"], ["dirty room","dormitory"], ["amleth","hamlet"], ["tinsel","listen","silent"] ]
https://www.glassdoor.com/Interview/Implement-a-function-all-anagram-groups-that-given-many-input-strings-will-identify-and-group-words-that-are-anagrams-o-QTN_739224.htm
"""

# O(MNLogN)
def all_anagram_groups(words):
    if not words:
        return None
    table = {}
    res = []
    for word in words:
        ws = "".join(sorted(word)).strip()
        if ws in table:
            table[ws].append(word)
        else:
            table[ws] = [word]

    for (key, val) in table.items():
        res.append(val)

    return res

arr = [ "pear","dirty room","amleth","reap","tinsel","hamlet","dormitory","listen","silent" ]
print all_anagram_groups(arr)