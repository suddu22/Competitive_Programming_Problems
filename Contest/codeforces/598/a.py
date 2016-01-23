__author__ = 'gr8h'
if __name__ == "__main__":


    n = int(raw_input())
    dict = {}
    for i in range(n):
        st = raw_input().split(" = ")
        dict[st[0]] = st[1]

    t = int(raw_input())
    for i in range(t):
        word_count = int(raw_input())
        sentance = raw_input().split()
        res = ""
        for word in sentance:
            res = res + dict[word] + " ".strip()
        print(res)

    '''s = raw_input()
    n = int(raw_input())

    for x in xrange(0, n):
        l, r, k = map(int, raw_input().split())

        k %= (r - l + 1)
        n = s[l-1:r]

        d = n[-k:]+n[:-k]

        s = s[:l-1]+d+s[r:]
    print s
    '''

    '''while n > 0:
        n -= 1
        ps = raw_input().split(' ')
        l = int(ps[0]) - 1
        r = int(ps[1]) - 1
        x = int(ps[2])
        k = (x % ((r+1)-(l+1)+1))

        while k > 0:
            k -= 1
            ch = st[r]
            st = st[0:r] + st[r+1:]
            st = st[:l] + ch + st[l:]
    print st


    k = (x % (len(st))) - 1
    n = int(raw_input())
    while n > 0:
        n -= 1
        x = int(raw_input())
        s = (x * (x+1))/2
        i = 1
        while i <= x:
            s -= (2*i)
            i *= 2
        print s'''