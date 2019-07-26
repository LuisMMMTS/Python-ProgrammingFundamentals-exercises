"""'

Write a recursive Python function `fib(n)', ' that returns the Fibonacci
series for `n', ' terms. Remember, the Fibonacci series is of a given number
is defined as the sum of the previous two Fibonacci numbers, with 0 and 1
being the base conditions.

'

"""

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)