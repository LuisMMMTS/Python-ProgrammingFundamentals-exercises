"""'

The factorial of a number can be written recursively. For example, _5!=4!*5_.
In other words:

'

"""

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)