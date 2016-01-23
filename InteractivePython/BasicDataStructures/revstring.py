from pythonds.basic.stack import Stack
from pythonds.basic.queue import Queue
import string


def revstring(sg):
    s = Stack()

    lst = [i for i in sg]
    res = []

    for c in lst:
        s.push(c)

    while not s.isEmpty():
        res.append(s.pop())

    return "".join(res)


# print revstring("hesham")


def parChecker(symbolString):
    s = Stack()

    balanced = True
    index = 0
    while balanced and index < len(symbolString):
        curr = symbolString[index]
        if curr in '([{':
            s.push(curr)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, curr):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(op, cl):
    opens = '([{'
    closes = ')]}'
    return opens.index(op) == closes.index(cl)


# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))
# print(parChecker('((()))'))
# print(parChecker('(()'))


def divideBy2(decNumber):
    s = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)

        decNumber //= 2

    res = []
    while not s.isEmpty():
        res.append(str(s.pop()))

    return "".join(res)


# print(divideBy2(42))


def baseConverter(decNumber, base):
    digits = string.digits + string.uppercase
    s = Stack()

    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber /= base

    res = []
    while not s.isEmpty():
        res.append(str(digits[s.pop()]))

    return "".join(res)


# print(baseConverter(25,8))
# print(baseConverter(26515,26))

def infixToPostfix(infixexpr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1, '^': 4}
    postfixList = []
    opStack = Stack()

    tokenList = infixexpr.split()
    for token in tokenList:
        if token in string.uppercase or token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postfixList.append(top)
                top = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


#print(infixToPostfix("10 + 3 * 5 / ( 16 - 4 )"))
#print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))


def evalPostfix(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        elif token in prec:
            op2 = operandStack.pop()
            op1 = operandStack.pop()
            res = doMath(token, op1, op2)
            operandStack.push(res)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    else:
        raise 'A3ml Bo Eh'

#print(evalPostfix('7 8 + 3 2 + /'))
#print(evalPostfix('17 10 + 3 * 9 / =='))











