"""
You have input arrays and one output. The output one contains only the elements that are only in one of the arrays
"""
"""
I face only one question. If you are given 2 array
A={3,1,2,4} B={1,4}.
Write a program to compare two arrays and create another array which holds the common values between two array!
https://www.glassdoor.com/Interview/I-face-only-one-question-If-you-are-given-2-array-A-3-1-2-4-B-1-4-Write-a-program-to-compare-two-arrays-and-create-an-QTN_497034.htm
"""


def arrayCommon(a1, a2):
    uniqu = set(a1)
    for num in a2:
        if num in uniqu:
            print num


a1 = [3, 1, 2, 4]
a2 = [1, 4]
arrayCommon(a1, a2)
