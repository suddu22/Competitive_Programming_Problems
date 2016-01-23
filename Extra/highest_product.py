import heapq


def highest_product(list_of_ints):
    ints = []
    for i in range(3):
        heapq.heappush(ints, abs(list_of_ints[i]))

    for i in range(3, len(list_of_ints)):
        heapq.heappush(ints, abs(list_of_ints[i]))
        heapq.heappop(ints)

    max_prod = 1
    while len(ints) > 0:
        pop = heapq.heappop(ints)
        max_prod *= pop

    return max_prod

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        print "3 needed"

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    highest_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for current in list_of_ints[2:]:
        highest_of_three = max(
            highest_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2
        )

        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)
    return highest_of_three

print highest_product_of_3([-10,-10,1,3,2]) # 300
print highest_product_of_3([2,3,4,5,6])