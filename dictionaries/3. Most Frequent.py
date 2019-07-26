"""'

Write a Python function `most_frequent(alist)', ' that, given a list `alist',
' of integers, using a dictionary, returns the most frequent element in
`alist', '. In case of ties, return the element with the greatest value.

'

"""

def most_frequent(alist):
    values={}
    for i in alist:
        if i not in values.keys():
            values[i]=1
        else:
            values[i]+=1
    return max(values.items(),key=lambda x: (x[1], x[0]))[0]