"""
"Smart substring"
Write a function that takes maximum 30 characters from a string but without cutting the words.

Full description:
"Featuring stylish rooms and moorings for recreation boats, Room Mate Aitana is a designer hotel built in 2013 on an island in the IJ River in Amsterdam."

First 30 characters:
"Featuring stylish rooms and mo"

Smarter approach (max 30 characters, no words are broken):
"Featuring stylish rooms and"

"""

def smart_substring(text, number):

    current_count = 0
    res = []
    for word in text.split():
        n = len(word)
        if current_count + n > number:
            return " ".join(res)
        else:
            res.append(word)
            current_count += n

text = "Featuring stylish rooms and moorings for recreation boats, Room Mate Aitana is a designer hotel built in 2013 on an island in the IJ River in Amsterdam."
print smart_substring(text, 30)


def process_string(text, number):
    text_arr = text.split(" ")
    final_string = ""
    for text_val in text_arr:
        if (len(text_val) + len(final_string)) > number:
            return final_string
        final_string = (final_string + " " + text_val).strip()
    return final_string
