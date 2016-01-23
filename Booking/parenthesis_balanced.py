"""
How to find whether a string of parenthesis is balanced or not.
Extended the question to find the matching parenthesis of a given parenthesis in a string.
Extended further to find all the matching parenthesis pairs in a huge file.
"""
"""
Balanced parenthesis
       Create function that will determine if the parenthesis are balanced in a given string.
         boolean isBalanced(string)
    Example :
             a(bcd)d => true
             (kjds(hfkj)sdhf => false
             (sfdsf)(fsfsf => false
             {[]}() => true
             {[}] => false
"""


# T: O(n), S:O(n)
def isBalanced(expr):
    st = []
    parenthesis = {')': '(',
                   '}': '{',
                   ']': '['}
    start = set(['(', '{', '['])

    for ch in expr:
        if ch in start:
            st.append(ch)
        elif ch in parenthesis:
            if parenthesis[ch] == st[len(st)-1]:
                st.pop()
            else:
                return False

    if len(st) > 0:
        return False

    return True

print "=== Balanced ==="
print isBalanced("a(bcd)d")
print isBalanced("(kjds(hfkj)sdhf")
print isBalanced("(sfdsf)(fsfsf")
print isBalanced("{[]}()")
print isBalanced("{[}]")


# T: O(n), S: O(2n)
def validPairs(expr):
    st = []
    parenthesis = {')': '(',
                   '}': '{',
                   ']': '['}
    start = set(['(', '{', '['])
    res = []
    for i in range(len(expr)):
        if expr[i] in start:
            st.append([expr[i], i])
        elif expr[i] in parenthesis:
            if st[len(st)-1][0] == parenthesis[expr[i]]:
                pop = st.pop()
                res.append(expr[pop[1]:i+1])  # + expr[i]

    return res

print "=== Valid Pairs ==="
print validPairs("a(bcd)d")
print validPairs("(kjds(hfkj)sdhf")
print validPairs("(sfdsf)(fsfsf")
print validPairs("{[]}()")
print validPairs("{[}]")


def matchingPair(exp, s):

    st = []
    res = []
    parenthesis = {')': '(',
                   '}': '{',
                   ']': '['}
    start = set(['(', '{', '['])

    for ch in exp:
        if ch in start:
            st.append(ch)
            #res.append(ch)

    for ch in s:
        if ch in parenthesis and parenthesis[ch] == st[len(st)-1]:
            st.pop()
            res.append(ch)

    return res

print "=== Matching Pairs ==="
print matchingPair("(he{sh[am", "dffhh(k)sh]aba}na)")


def validCompination(left, right, res=[]):

    if right == 0:
        print "".join(res)
        return

    if left > 0:
        validCompination(left-1, right, res + ['('])

        if left < right:
            validCompination(left, right-1, res + [')'])
    else:
        validCompination(left, right-1, res + [')'])

print "=== Compinations ==="
validCompination(3, 3)