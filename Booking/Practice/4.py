# coding=utf-8
"""
$a = [3, 1, 4, 5, 19, 6];

$b = [14, 9, 22, 36, 8, 0, 64, 25];
# Some elements in the second array are squares.
# Print elements that have a square root existing in the first array.
# $b[1] = 9, it’s square root is 3 ($a[0])
# $b[3] = 36, it’s square root is 6 ($a[5])
# $b[7] = 25, it’s square root is 5 ($a[3])

# Result:
# 9
# 36
# 25

"""
def array_square(a1, a2):
    if not a1 and not a2:
        return None
    table = set()
    for num in a1:
        table.add(num*num)

    for num in a2:
        if num in table:
            print num

a = [3, 1, 4, 5, 19, 6]
b = [14, 9, 22, 36, 8, 0, 64, 25]
array_square(a, b)