"""
 You have data structure my
 $users = [ { name ='John', score =10, },
    { name 'Bob', score = 1, },
    { name ='Carlos', score = 5 },
    { name ='Alice', score = 5, },
    { name ='Donald', score = 7 } ];
now u have to arrange the name with highest to lower score,
if score is same than in alphabetical order #expected output: # John # Donald # Alice # Carlos # Bob
https://www.glassdoor.com/Interview/You-have-datastructure-my-users-name-and-gt-John-score-and-gt-10-QTN_636255.htm
"""
"""
Can be done easily, if we use a stable sort.
I dont know perl; but I am guessing the provided data structure is a hashtable (or a dictionary!)
sorted_names = sorted(users.keys()) this will sort all names in alphabetical order Now python's sort is stable;
so we can simply finish this by: return sorted(sorted_names, key=lambda x: users[x], reverse=True)
"""
users_dict = dict(John=10, Bob=1, Carlos=5, Alice=5, Donald=7)

def sortDictByValueKey(users_dict):

    sorted_names = sorted(users_dict.keys())
    sorted_users = sorted(sorted_names, key= lambda x: users_dict[x], reverse=True)

    print(sorted_users)

sortDictByValueKey(users_dict)


"""
Sort the content of the a file based on second field.
      Example  :
                 Input file:
                              Jervie,12,M
                              Jaimy,11,F
                              Tony,23,M
                             Janey,11,F

                Output file:
                              Jaimy,11,F
                              Janey,11,F
                              Jervie,12,M
                              Tony,23,M

        Total file size is 4G, but you only have 1G of RAM.
"""
blockNames = []
def partitioner(filePath, bufferSize):

    file = open(filePath, 'r')
    for line in file:
        row = line.strip('\w+')
        if row[1] in range(1, 25):
            blockWrite("1_25")



def blockWrite(blockName, data):
    file = open(blockName, 'w')
    file.write(data)
    file.close()









