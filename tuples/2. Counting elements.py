"""'

Write a function `count_until(tup)', ' that, given a tuple `tup', ', returns
the number of elements in it before an element of the type tuple appears. If
there isn’t a nested tuple, it should return -1.

'

"""

def count_until(tup):
    for i in range(len(tup)):
        if type(tup[i])==tuple:
            return i
    return -1