import string


def listsum(lst):
    if len(lst) == 1:
        return lst[0]

    return lst[0] + listsum(lst[1:])


# print(listsum([1, 3, 5, 7, 9]))


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    return toStr(n / base, base) + convertString[n % base]


# print(toStr(1453,16))

def strRev(strtorev):
    if len(strtorev) <= 1:
        return strtorev

    return strRev(strtorev[1:]) + strtorev[0]

def listRev(l):
    if len(l) <= 1:
        return l

    res = [l[-1]] + listRev(l[:-1])
    return res

print(listRev([1,2,3,4,5]))
# print(strRev("hesham"))

def numRev(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num /= 10

    return rev_num


def removeWhite(s):
    res = "".join([ch for ch in s if ch not in string.punctuation + " "])
    return res


def isPal(s):
    s = removeWhite(s)
    rs = strRev(s)
    return s == rs


def isPal2(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and isPal2(s[1:-1])


# print(isPal2(removeWhite("x")),True)
# print(isPal2(removeWhite("radar")),True)
# print(isPal2(removeWhite("hello")),False)
# print(isPal2(removeWhite("")),True)
# print(isPal2(removeWhite("hannah")),True)
# print(isPal2(removeWhite("madam i'm adam")),True)

def moveTower(h, a, b, c):
    if h >= 1:
        moveTower(h - 1, a, c, b)
        print("moving disk from", a, "to", c)
        moveTower(h - 1, c, b, a)

#moveTower(3, "A", "B", "C")

factorial_dict = {}
def factorial(n):
    if n <= 1:
        return 1
    if n in factorial_dict:
        return factorial_dict[n]

    res = n * factorial(n-1)
    factorial_dict[n] = res

    return res

#print(factorial(4))

fibo_dict = {}
def fibo(n):
    if n <= 1:
        return 1

    if n in fibo_dict:
        return fibo_dict[n]

    res = fibo(n-1) + fibo(n-2)
    fibo_dict[n] = res

    return res

#print(fibo(5))

def paskal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]

    new_row = [1]
    res = paskal(n-1)
    last = res[-1]
    for i in range(len(last)-1):
        new_row.append(last[i] + last[i+1])
    new_row += [1]
    res.append(new_row)
    return res

print(paskal(4))

def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

print(triangle(4))