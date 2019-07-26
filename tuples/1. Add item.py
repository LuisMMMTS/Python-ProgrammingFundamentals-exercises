"""'

Write a Python function `add_item(tup, idx, item)', ' that, given a tuple
`tup', ', inserts the value `item', ' at position `idx', '. If `idx', ' points
to the beginning or the end of the tuple, it should replace the old value.
Assume that index always holds a valid value.

'

"""

def add_item(tup, idx, item):
    if idx==len(tup)-1:
        tup=((tup[:-1]+(item,)))
    elif idx==0:
        tup=((item,)+(tup[1:]))
    else:
        tup=(tup[:idx]+(item,)+tup[idx:])
    return tup