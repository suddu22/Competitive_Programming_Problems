
# t.put('a', 5, 'apple')
# t.put('a', 5, 'pear')
# t.put('a', 10, 'aardvark')


# t.get('a', 8) #=> 'pear'

#
# keys
#  'a' -> (5,apple) -> (10,'aardvark') <- BSTree
#  'b'


# keys
#  5 -> apple
#  8 -> None
#  9 -> None
# 10 -> aardvark

dict = {}


def put(key, ts, val):
    if key not in dict:
        dict[key] = {'ts': ts, 'val': val, 'left': None, 'right': None}
    else:
        put_rec(dict[key], ts, val)


def put_rec(curr, ts, val):
    if ts > curr['ts']:
        if curr['right'] is None:
            curr['right'] = {'ts': ts, 'val': val, 'left': None, 'right': None}
        else:
            put_rec(curr['right'], ts, val)
    else:
        if curr['left'] is None:
            curr['left'] = {'ts': ts, 'val': val, 'left': None, 'right': None}
        else:
            put_rec(curr['left'], ts, val)


def get(key, ts):
    if key in dict:
        return get_rec(dict[key], ts)
    else:
        return None


def get_rec(curr, ts):

    if curr is None:
        return None

    if ts > curr['ts']:
        if curr['right'] is None:
            return curr['val']
        else:
            return get_rec(curr['right'], ts)
    else:
        if curr['left'] is None:
            return curr['val']
        else:
            return get_rec(curr['left'], ts)

put('a',5,'apple')
put('a',10,'lol')
put('a',7,'pear')

put('a',2,'ahh')


print get('a', 8)
print get('a',15)
print get('a',4)