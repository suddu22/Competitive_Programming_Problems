"""
We've got a book.txt that contains text of a book written with English alphabet.

Transform the words in this book into numbers. For simplicity, escape all non English alphabet characters.
Print the output on STDOUT.

Example IN:

This is a sample
for this problem.
It is short,
compared to a book.

Example OUT:

1 2 3 4
5 1 6
7 2 8
9 10 3 11

Note: no need to preserve newlines!
"""
import re
def words_to_numbers(file_name):

    if not file_name:
        return None

    tabel = {}
    current_index = 1
    stream = open(file_name, 'r')
    for line in stream:
        line = re.split('\W+', line.lower())
        for word in line:
            if word == "":
                continue
            if word not in tabel:
                tabel[word] = current_index
                print current_index,
                current_index += 1
            else:
                print tabel[word],
        print

words_to_numbers("11")