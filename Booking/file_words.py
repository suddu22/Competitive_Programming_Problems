"""
You have the file with word at a single line.
#input sample file
abactor
abaculus
abacus
Abadite
.
.
Zyrenian

#Output
******************************************************************a
*************b
**********************************c
**********************d
*******************************************************************************e

a) you have to count the character and create a histogram in alphabetical order.
b) now you have to produce a histogram with max 80 character in line in reference to max count
c) now same out based histrogram based on the character count

Histogram

"""
import string

def charCount(fileName):
    char_count = {}
    max_count = 0
    with open(fileName, 'r') as f:
        content = f.readlines()

    for word in content:
        word = str(word).lower()
        for char in word:
            if char not in string.lowercase:
                continue
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

            if char_count[char] > max_count:
                max_count = char_count[char]

    return char_count, max_count

def histogram1(fileName, limit):
    char_count, max_count = charCount(fileName)
    adj = 0
    if max_count > limit:
        adj = limit - max_count
    elif max_count < limit:
        adj = max_count - limit

    char_sorted = sorted(char_count.keys())
    for char in char_sorted:
        ratio = char_count[char] + adj
        if ratio < 0:
            ratio = 0
        char_hist = ['*'] * ratio
        char_hist.append(char)
        print "".join(char_hist)

def histogram(fileName, limit):
    char_count, max_count = charCount(fileName)

    char_sorted = sorted(char_count.keys())
    for char in char_sorted:
        ratio = char_count[char] / limit
        char_hist = ['*'] * ratio
        char_hist.append(char)
        print "".join(char_hist)


histogram1('file_words', 80)


def other():
    with open('file', 'r') as f:
            contents = f.readlines();

    result = {}

    #gather
    for word in contents:
            for letter in word:
                    if not result.has_key(letter):
                            result[letter] = 0;
                    result[letter] = result[letter] + 1;

    #represent
    maxval = result[max(result.keys(), key=lambda x: result[x])]

    for key in sorted(result.keys()):
            ratio = int((float(result[key]) / float(maxval)) * 80);
            string = '';
            i = 0;
            for i in  xrange(ratio):
                    string = string + '*';
                    i = i + 1;

            print '%s%s' % (string, key)