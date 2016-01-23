# put('a', 5, 'aapl')
# put('a', 10, 'msft')
# put('a', 16, 'uber')

# put('abc', 16, 'uber')


# put('b', 10, 'goog')

# get('a',12) ---> msft
# get('b',10) ->> goog

# dict --> Key: 'a' + '_' + 12
# Value: aapl

dict = {}
def put(key, t, word):

    # dict[key] = value
    if key in dict:
        dict_curr = dict[key]
        #print dict_curr
        while(dict_curr != None and dict_curr['next'] != None):
            dict_curr = dict_curr['next']

        dict_curr['next'] = {'next':None, 'ts':t, 'val':word}

#        ndict = {'next':None, 'ts':t, 'val':word}
    else:
        ndict = {'next':None, 'ts':t, 'val':word}
        dict[key] = ndict

def get(key, t):
    list = dict[key]
    temp = list['val']
    while(list != None and list['next']['next'] != None and list['ts'] != t):

        list = list['next']
        temp = list['val']

    if list['val'] == None:
        temp = list['val']

    return temp


put('a', 5, 'aapl')
put('a', 10, 'msft')
put('a', 16, 'uber')
put('b', 10, 'goog')

print get('a', 8)

#print dict