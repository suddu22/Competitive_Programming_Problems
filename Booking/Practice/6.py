"""
Given coins of various denominations and an amount.
You have to return the minimum number of coins and their denominations required to equal the amount.
I took DP approach to give the solutions and the interviewers seemed to be happy with it.
"""

def change_easy(change, sets):
    if change in sets:
        return change
    sets = sorted(sets, reverse=True)
    i = 0
    count = 0
    while change > 0:
        if change >= sets[i]:
            change = change - sets[i]
            count += 1
        else:
            i += 1
    return count

print change_easy(63, [25, 10, 5, 1])


def change_rec(change, sets):
    if change in sets:
        return 1
    min_coin = change
    for i in [st for st in sets if st <= change]:
        res = 1 + change_rec(change - i, sets)
        if res < min_coin:
            min_coin = res

    return min_coin

#print change_rec(63, [25, 10, 5, 1])

def change_rec_memo(change, sets, memo={}):
    if change in sets:
        return 1
    if change in memo:
        return memo[change]
    min_coin = change
    for i in [st for st in sets if st <= change]:
        res = 1 + change_rec_memo(change - i, sets, memo)
        if res < min_coin:
            min_coin = res
            memo[change] = min_coin
    return min_coin

print change_rec_memo(63, [25, 10, 5, 1])

def change_dp(change, sets):

    counts = [0] * (change+1)
    for cent in range(change+1):
        coin_count = cent
        for coin in [st for st in sets if st <= cent]:
            if counts[cent - coin] + 1 < coin_count:
                coin_count = counts[cent - coin] + 1
        counts[cent] = coin_count
    return counts[change]

print change_dp(63, [25, 10, 5, 1])

def change_dp_used(change, sets):

    count = [0] * (change+1)
    usedCoins = {}
    for cent in range(change+1):
        min_coins = cent
        newCoin = 1
        for coin in [st for st in sets if st <= cent]:
            if count[cent - coin] + 1 < min_coins:
                min_coins = count[cent - coin] + 1
                newCoin = coin
        count[cent] = min_coins
        usedCoins[cent] = newCoin

    return usedCoins

print change_dp_used(63, [25, 10, 5, 1])