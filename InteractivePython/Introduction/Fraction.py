def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        _int_error_msg = u'Only integers are acceptable'
        if not isinstance(top, int):
            raise TypeError(_int_error_msg)
        if not isinstance(bottom, int):
            raise TypeError(_int_error_msg)

        if bottom < 0:
            bottom *= -1
            top *= -1

        common = gcd(top, bottom)
        self.num = int(top // common)
        self.den = int(bottom // common)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        #common = gcd(newnum, newden)
        #return Fraction(newnum // common, newden // common)

        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __div__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __iadd__(self, other):
        return self + other


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
