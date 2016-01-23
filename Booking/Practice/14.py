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


def isBalanced(text):
    if not text:
        return True

    start = set(["(", "{", "["])
    match = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []

    for ch in text:
        if ch in start:
            stack.append(ch)
        elif ch in match:
            if match[ch] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False
    return True

print "=== Balanced ==="
print isBalanced("a(bcd)d")
print isBalanced("(kjds(hfkj)sdhf")
print isBalanced("(sfdsf)(fsfsf")
print isBalanced("{[]}()")
print isBalanced("{[}]")

def validPairs(text):
    if not text:
        return True

    start = set(["(", "{", "["])
    match = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    res = []

    for i in range(len(text)):
        ch = text[i]
        if ch in start:
            stack.append([ch, i])
        elif ch in match:
            if match[ch] == stack[len(stack)-1][0]:
                pop = stack.pop()
                res.append(text[pop[1]:i+1])
    return res

print "=== Valid Pairs ==="
print validPairs("a(bcd)d")
print validPairs("(kjds(hfkj)sdhf")
print validPairs("(sfdsf)(fsfsf")
print validPairs("{[]}()")
print validPairs("{[}]")