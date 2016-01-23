"""
Given coins of various denominations and an amount.
You have to return the minimum number of coins and their denominations required to equal the amount.
I took DP approach to give the solutions and the interviewers seemed to be happy with it.
"""


def coins_greedy(clist, change):
    clist = [25, 10, 5, 1]
    coin_count = 0
    res = []
    i = 0

    while i < len(clist):
        if change >= clist[i]:
            change -= clist[i]
            coin_count += 1
            res.append(clist[i])
        else:
            i += 1
    print res, coin_count

"""
Time complexity of recursive algorithm is exponential
"""
def coins_rec(clist, change):
    min_coin = change
    if change in clist:
        return 1

    for c in [coin for coin in clist if coin <= change]:
        num = 1 + coins_rec(clist, change - c)
        if num < min_coin:
            min_coin = num

    return min_coin


def coins_rec_memoization(clist, change, saved):
    min_coin = change
    if change in clist:
        return 1
    elif change in saved:
        return saved[change]
    else:
        for c in [coin for coin in clist if coin <= change]:
            num = 1 + coins_rec_memoization(clist, change - c, saved)
            if num < min_coin:
                min_coin = num
                saved[change] = min_coin
    return min_coin

"""
Dynamic Programming solution is O(n*sum)
"""
def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]


def coin_dp(clist, change, minCoins):
    for cent in range(change + 1):
        coin_cnt = cent
        for coin in [c for c in clist if c <= cent]:
            if minCoins[cent - coin] + 1 < coin_cnt:
                coin_cnt = minCoins[cent - coin] + 1
        minCoins[cent] = coin_cnt
    return minCoins[change]


def coin_dp_used(clist, change, minCoins, usedCoins):
    for cent in range(change + 1):
        coin_cnt = cent
        newCoin = 1
        for coin in [c for c in clist if c <= cent]:
            if minCoins[cent - coin] + 1 < coin_cnt:
                coin_cnt = minCoins[cent - coin] + 1
                newCoin = coin
        minCoins[cent] = coin_cnt
        usedCoins[cent] = newCoin
    return minCoins[change]


def printUsedCoins(usedCoins, change):
    coin = change
    while coin > 0:
        c = usedCoins[coin]
        print(c)
        coin = coin - c


#print coin_dp([1, 5, 10, 21, 25], 63, {})
usedCoins = {}
print coin_dp_used([1, 5, 10, 21, 25], 63, {}, usedCoins)
printUsedCoins(usedCoins, 63)
