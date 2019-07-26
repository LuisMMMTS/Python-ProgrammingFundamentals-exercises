"""'

Define a function `count_elems(tup)', ' that, given a tuple `tup', ', returns
a new tuple in which each element corresponds to: the number of elements in
the element at the same position in `tup', ', if a tuple or a list; the number
of characters, if a string; 1 otherwise.

'

"""

def count_elems(tup):
    new_tup=()
    for i in (tup):
        if type(i)!=tuple and type(i)!=list and type(i)!=str:
            new_tup+=1,
        else:
            new_tup+=(len(i),)
    return new_tup