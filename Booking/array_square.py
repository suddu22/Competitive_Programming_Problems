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

"""
1) Insert 2nd array values into hash map
2) Iterate through 1st array and square each value
3) Check for squared value in hash map and print match

If you replace unordered_map ( find() runs O(n) time as worst case) with your own hash map and assume no collisions,
this solution runs in O(n) time complexity.
"""

def square(a1, a2):

    if a1 is [] and a2 is []:
        return None

    a2Set = set()
    for n in a2:
        a2Set.add(n)

    for n in a1:
        nn = n * n
        if nn in a2Set:
            print(nn)

a1 = [3, 1, 4, 5, 19, 6]
a2 = [14, 9, 22, 36, 8, 0, 64, 25]
square(a1, a2)

def findSquaresInArray(a1, a2):
    n1 = len(a1)
    n2 = len(a2)

    if n2 == 0 or n1 == 0:
        return None

    hashmap = {}
    results = []

    for el in a1:
        hashmap[el] = True

    for el in a2:
        root = pow(el, 0.5)
        int_root = int(root)
        if root != int_root:
            continue

        pos_root = hashmap.get(int_root)
        neg_root = hashmap.get(-1 * int_root)

        if pos_root == True:
            results.append(el)

        elif neg_root == True:
            results.append(el)

        else:
            continue

    return results
