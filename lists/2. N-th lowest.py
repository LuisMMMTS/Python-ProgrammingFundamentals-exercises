"""'

Write a Python function `nth_lowest(lnum, n)', ' that, given a list of numbers
`l', ' and a positive integer `n', ', returns the `n', '-th lowest value in
the list. Assume `n', ' always holds a valid value (i.e. does not go out of
bounds) and that the list never has repeated values.

'

"""

def nth_lowest(lnum, n):
    lnum.sort()
    return lnum[n-1]