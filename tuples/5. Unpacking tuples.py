"""'

Write a Python function `unpack_rev(atuple)', ' to unpack the tuple `atuple',
' and return the items as a string, separated by spaces and in **reverse**
order. The tuple does not contain compound items.

'

"""

def unpack_rev(atuple):
    s=""
    for i in atuple[::-1]:
        s=s+str(i)+" "
    return s