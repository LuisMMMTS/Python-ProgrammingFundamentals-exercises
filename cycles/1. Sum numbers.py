"""'

Define a function `f(n)', ' that returns the sum of numbers 1+2+...+n.

'

"""

def f(n):
    soma=0
    for i in range(n+1):
        soma+=i
    return soma