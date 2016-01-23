import math
import string
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A <= 0:
            return 0
        if A == 1:
            return [1]

        res = [1, A]
        sqrtN = int(A**0.5)
        for i in range(2, sqrtN):
            if A % i == 0:
                res.append(i)
                if math.sqrt(A) != i:
                    res.insert(0, A/i)
        if A%sqrtN == 0:
            res.append(sqrtN)
            if sqrtN**2 != A:
                res.append(A/sqrtN)
        res.sort()
        return res

    def isPrime(self, A):
        if A == 0 or A == 1:
            return 0

        sqrtn = int(A**0.5)
        for i in range(2, sqrtn+1):
            if A % i == 0:
                return 0

        return 1

    def sieve(self, A):
        if A <= 1:
            return None

        sie = [-1] * (A + 1)
        sie[0] = 0
        sie[1] = 0
        res = []
        for i in range(2, A+1):
            if sie[i] == -1:
                res.append(i)
                sie[i] = 1

                j = 0
                while (i*j) <= A:
                    index = i*j
                    if index > i:
                        sie[index] = 0
                    j += 1

        return res

    def primesum(self, A):
        for i in range(2, A):
            if self.isPrime(i) and self.isPrime(A-i):
                return i, A-i


    def isPrime(self, num):
        if num < 2:
            return False

        for i in xrange(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True

    ####
    def primesum(self, n):
        for i in xrange(2, n):
            if self.is_prime(i) and self.is_prime(n - i):
                return i, n - i

    def is_prime(self, n):
        if n < 2:
            return False

        for i in xrange(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

    ####
    def isPower(self, A):
        if A == 1:
            return True

        sqrtn = int(A**0.5)
        for i in range(2, sqrtn+1):
            p = 2
            curr_power = int(math.pow(i, p))
            while curr_power < A:
                p += 1
                curr_power = int(math.pow(i, p))

            if curr_power == A:
                return True

        return False

    ##
    def baseConverter(self, A):
        if A == 0:
            return 0

        res = []
        base = 26
        num = A - 1
        a = ord('A')

        while num >= 0:
            re = num % base
            num /= base
            num -= 1

            x = chr(a + re)
            res.append(x)

        return "".join(res)

s = Solution()
print s.baseConverter(27)