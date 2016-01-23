import sys
import math
import random

__author__ = 'gr8h'

if __name__ == "__main__fff":

    def findProd(strA):
        ret = 1
        for a in strA:
            ret *= int(a)

        return str(ret)

    def colorful(self, A):
        self = {}
        strA = str(A)
        for s in strA:
            if s in self:
                return 0
            else:
                self[s] = 1

        n = len(strA)
        for i in range(2, n+1):
            for j in range(n-i+1):
                num = strA[j:j+i]
                ret = findProd(num)
                if ret in self:
                    return 0
                else:
                    self[ret] = 1
        return 1



    print colorful([], 23)

    def canAddQ(matrix, row, col):
        n = len(matrix)
        for i in range(0, col):
            if matrix[row][i] == 1:
                return False
        j = col
        for i in range(row, 0, -1):
            if j >= 0 and matrix[i][j] == 1:
                return False
            j -= 1

        j = col
        for i in range(row, n):
            if j >= 0 and matrix[i][j] == 1:
                return False
            j -= 1
        return True


    def solveNQ(matrix, col):
        if col >= len(matrix):
            return True

        for i in range(0, len(matrix)):
            if canAddQ(matrix, i, col):
                matrix[i][col] = 1

                if solveNQ(matrix, col + 1):
                    return True

                matrix[i][col] = 0

        return False


    def solveNQueens(self, A):

        matrix = [[0 for x in range(A)] for x in range(A)]

        if not solveNQ(matrix, 0):
            return False

        return matrix


    #print solveNQueens([], 3)

    '''n = int(raw_input())
    banks = list(map(int, raw_input().split(' ')))

    has_negative = True
    result = 0
    while has_negative:

        for cap in range(0, n):
            if banks[cap] < 0:
                next_cap = cap + 1
                prev_cap = cap - 1
                if next_cap >= n:
                    next_cap -= n
                else:
                    if prev_cap < 0:
                        prev_cap = n + prev_cap

                fix = -1 * banks[cap]
                banks[cap] = fix
                banks[next_cap] -= fix
                banks[prev_cap] -= fix
                result += 1

        for v in banks:
            has_negative = False
            if v < 0:
                has_negative = True
                break

    print result'''

    '''def grayCode(self, A):
        if A <= 0:
            return

        lst = ['0','1']

        while A > 0:
            nlst = []

            for i in lst:
                nlst.append(str(0) + str(i))

            lst.reverse()
            for i in lst:
                nlst.append(str(1) + str(i))

            lst = nlst
            A = A -1

        self = []
        for b in nlst:
            self.append(int(b,2))

        return self

    def gray_code_generate(n):

        if n <= 0:
            return

        lst = ['0','1']

        while n > 0:
            nlst = []

            for i in lst:
                nlst.append(str(0) + str(i))

            lst.reverse()
            for i in lst:
                nlst.append(str(1) + str(i))

            lst = nlst
            n = n -1

        res = []
        for b in nlst:
            res.append(int(b,2))

        return res

    def permute(self, A):

        n = len(A)
        f = math.factorial(n)
        np = f / n

        self = permute_rec([], A, 3)
        return self

    def permute_rec(result, A, np):

        if len(A) == np:
            return A

        for num in A:
            new_a = A[:]
            new_a.remove(num)
            rev_a = new_a[:]
            rev_a.reverse()

            for x in range(0, len(new_a)):
                result.append([num] + permute_rec(result, new_a, np))
                result.append([num] + permute_rec(result, rev_a, np))

        return result

    print permute([], [1,2,3, 4])'''

    '''def is_list(p):
        return isinstance(p, list)

    def deep_count(p):
        count = 0
        for e in p:
            count = count + 1
            if is_list(e):
                count = count + deep_count(e)
        return count

    print deep_count([1, [1, 2, [3, 4]]])'''

    '''n,t = map(int,raw_input().split())
    d = n
    n = 10**n-1
    n = n - n%t
    if n == 0:
        print -1
    else:
        print n'''

    '''n, d = map(int, raw_input().split())
    target1 = 10**n/10
    target2 = 10**n - 1
    x = d
    found = False
    while True:
        if x >= target1 and x <= target2:
            if x % d == 0:
                print x
            else:
                print -1
            break
        else:
            if x < target1:
                x = x * d
            else:
                print -1
                break'''

    '''n, d = map(int, raw_input().split())

    if d > n/2:
        d = n/2

    target = n + 1
    sets = []
    i = 1
    while i <= n:
        rem = target - i
        if [i, rem] not in sets:
            sets.append([rem, i])
        i += 1
    sys.stdout.write(str(len(sets) + d))
    #print (len(sets) + d)'''

    '''n, d = map(int, raw_input().split())

    print int(math.ceil(n/2))

    res = int(math.ceil(n/2) + d)

    print res'''

    '''n = int(raw_input())
    pc = list(map(int, raw_input().split(' ')))

    dir = 0
    dic = {}
    for i in range(0, n):
        if pc[i] in dic:
            dic[pc[i]].append(i)
        else:
            dic[pc[i]] = [i]

    #print dic
    for i in range(0, n):
        val = dic[pc[i]]
        if val[0] <> i:
            dir += 1

        if len(val) > 1:
            val = val[:1]
            dic[pc[i]] = val
        else:
            del dic[pc[i]]


    print dir'''

    '''print pc
    print dic
    pc.sort()
    print pc'''

    '''n = int(raw_input())
    hl = [0] * (n+1)
    vl = [0] * (n+1)
    nn = n**2
    for i in xrange(nn):
        h, v = map(int, raw_input().split())
        if hl[h] == 0 and vl[v] == 0:
            hl[h] = vl[v] = 1
            print i+1'''

    '''n = int(raw_input())
    a = list(map(int, raw_input().split(' ')))
    b = [0]*n
    mx = a[n-1]
    for i in range(n-2, -1, -1):
        b[i] = max(0, mx-a[i]+1)
        if a[i] > mx:
            mx = a[i]
    for r in b:
        print r'''
