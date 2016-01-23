
def _0():

    sp = map(int, raw_input().split())
    tr = map(int, raw_input().split())

    for i in range(len(sp)):
        sp[i] -= tr[i]
        if sp[i] > 0:
            s = sp[i] / 2
            sp[i] /= 2

    spt = sum([int(i) for i in sp])
    if(spt >= 0):
            print 'Yes'
    else:
        print 'No'

_0()