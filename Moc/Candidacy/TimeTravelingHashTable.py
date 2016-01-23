

# t.put('a', 5, 'apple')
# t.put('a', 5, 'pear')
# t.put('a', 10, 'aardvark')


# t.get('a', 8) #=> 'pear'

#
# keys
#  'a' -> (5,apple) -> (10,'aardvark') <- BSTree
#  'b'
#
#
# keys
#
#  5 -> apple
#  8 -> None
#  9 -> None
# 10 -> aardvark
#
#
# 

hash = {}

def recInsert(curr, val, ts):

    
    #base case
    #if curr is None:
    #    return
    
    
    if ts > curr['ts']:
        
        if curr['right'] is None:
            curr['right'] = {'payload': val, 'ts': ts, 'left': None, 'right': None}
        
        else:
            recInsert(curr['right'], val, ts)
            

    else: # "<="
        
        if curr['left'] is None:
            curr['left'] = {'payload': val, 'ts': ts, 'left': None, 'right': None}
        else:
            recInsert(curr['left'], val, ts)
        
        
        
        
        
def put(key, ts, val):
    
    # new entry
    if key in hash:
        
        #search through BST, insert elem
        recInsert(hash[key], val, ts)
        
    else:
        hash[key] = {'payload': val, 'ts': ts, 'left': None, 'right': None}
    



def recGet(curr, ts):
    
    #base case
    if curr is None:
        return None
    
    
    #base case 2 -- become apparent later
    
    
    
    if ts > curr['ts']:
    
        if curr['right'] is None:
            return curr['payload']
        
        else:
            return recGet(curr['right'],ts)
            
    
    elif ts == curr['ts']:
        

        return curr['payload']
        
    else:
        
        if curr['left'] is None:
            return None
        
        else:
            return recGet(curr['left'], ts)
    
    
    
def get(key,ts):
    
    if key in hash:
        
        return recGet(hash[key], ts)
    
    else:
        return None
    
    
    

put('a',5,'apple')
put('a',10,'lol')
put('a',7,'pear')

put('a',2,'ahh')


print get('a', 8)
print get('a',15)
print get('a',4)

#get('a',8)