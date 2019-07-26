"""'

Write a Python function `rotate_list(l)', ' that, given a list `l', ' of
length >= 3, shifts its elements to the left 3 times, returning the new list.
If an element is at the beginning, it should circle back to the end.

'

"""

def rotate_list(l):
    return l[3:]+l[:3]