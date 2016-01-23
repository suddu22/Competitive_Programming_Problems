#!/usr/bin/env python

import sys

current_word = None
current_count = 0
current_sum = 0.0
word = None

for line in sys.stdin:
    line = line.strip()
    # parse the input we got from mapper.py
    word, word_length = line.split('\t', 1)

    if current_word == word:
        current_count += 1
        current_sum += word_length

    else:
        if current_word:
            print '%s\t%s' % (current_word, current_sum / current_count)
        current_word = word
        current_count = 1
        current_sum = word_length

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_sum / current_count)