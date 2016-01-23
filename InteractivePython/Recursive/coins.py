def recMC(coinValueList, change):
    min_coin = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            num_coin = 1 + recMC(coinValueList, change - i)
            if num_coin < min_coin:
                min_coin = num_coin
    return min_coin


# print(recMC([1,5,10,25],63))

def recDC(coinValueList, change, knownResults):
    min_coin = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif change in knownResults:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            num_coin = 1 + recDC(coinValueList, change - i, knownResults)
            if num_coin < min_coin:
                min_coin = num_coin
            knownResults[change] = min_coin
    return min_coin


# print(recDC([1,5,10,25],63, {}))


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)


main()
