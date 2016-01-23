

def twoSum(A, B):
    sum_dict = {}
    for i in range(len(A)):
        if A[i] in sum_dict:
            index = sum_dict[A[i]]
            i1 = index + 1
            i2 = i + 1
            print "index1 = %d, index2 = %d" % (i1, i2)
            return
        else:
            if B - A[i] not in sum_dict:
                sum_dict[B - A[i]] = i

    return None

A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
B = -3
# 4 8
#twoSum(A, B)

A = [ -10, -10, -10 ]
B = -5
# None
#twoSum(A, B)


def fourSum(A, B):
    if not A:
        return []

    res = []
    n = len(A)
    A = sorted(A)

    for i in range(n):
        for j in range(i + 1, n):
            k = j + 1
            l = n - 1

            while k < l:
                fsum = A[i] + A[j] + A[k] + A[l]
                if fsum == B:
                    res.append([A[i], A[j], A[k], A[l]])
                    k += 1
                    l -= 1
                elif fsum > B:
                    l -= 1
                else:
                    k += 1

    return res

A = [1, 0, -1, 0, -2, 2]
B = 0
print fourSum(A, B)
