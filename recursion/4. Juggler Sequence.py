"""'

Write a recursive Python function `juggler(n, p)', ' that, given two integers
`n', ' and `p', ', calculates the `p', '-th term in the juggler sequence for
`n', '. The juggler sequence for a non-negative integer `n', ' is defined as
follows:

'

"""

def juggler(n,p):
    if p==0:
        return n
    else:
        if juggler(n,p-1)%2==0:
            return int(juggler(n,p-1)**(1/2))
        else:
            return int(juggler(n,p-1)**(3/2))