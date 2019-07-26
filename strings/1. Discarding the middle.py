"""'

Write a Python function `discard_middle(s)', ' that, given a string `s', ',
returns a new string consisting of its first and last 2 characters. If the
string is less or equal to 3 characters, the result should be the empty
string.

'

"""

def discard_middle(s):
    if len(s)>3:
        return (s[0]+s[1]+s[-2]+s[-1])
    else:
        return""