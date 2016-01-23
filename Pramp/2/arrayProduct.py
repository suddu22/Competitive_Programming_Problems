def calcProductArray(arr):
    n = len(arr)
    productArr = [1] * n

    product = 1
    for i in range(n):
        productArr[i] *= product
        product *= arr[i]

    product = 1
    for i in range(n-1, -1, -1):
        productArr[i] *= product
        product *= arr[i]

    return productArr


arr = [2, 7, 3, 4]
#print calcProductArray(arr)

# O(n) time and O(n)O(n) space.
def get_products_of_all_ints_except_at_index(arr):

    n = len(arr)
    before = [1] * n
    after = [1] * n
    res = [1] * n

    for i in range(1, n):
        before[i] = arr[i-1] * before[i-1]

    for i in range(n-2, -1, -1):
        after[i] = arr[i+1] * after[i+1]

    for i in range(n):
        res[i] = before[i] * after[i]

    return res

print get_products_of_all_ints_except_at_index([1,2,6,5,9])
