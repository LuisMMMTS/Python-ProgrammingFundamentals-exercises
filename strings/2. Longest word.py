"""'

Write a Python function `longest(s)', ' that, given a string `s', ', returns
the length of its longest word.

'

"""

def longest(s):
    big_size=0
    for word in s.split():
        if len(word)>big_size:
            big_size=len(word)
    return big_size