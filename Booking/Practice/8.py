"""
Convert number above in hexadecimal 312312 Ex.
255 = FF
254 -&gt;
254 div 16 = 14, int(254/16) = 15. -&gt; F, E
Later I found the detailed Division-remainder in source base
http://en.wikipedia.org/wiki/Hexadecimal#Division-remainder_in_source_base

"""
import string
def base_converter(num, base):

    alpha = string.digits + string.uppercase
    s = []
    while num > 0:
        rem = num % base
        s.append(rem)
        num = num / base

    res = []
    while len(s) > 0:
        res.append(str(alpha[s.pop()]))

    return "".join(res)
