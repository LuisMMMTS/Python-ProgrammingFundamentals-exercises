"""'

Write a Python function `fib(n)', ' that returns a list of the first `n', '
[Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number). The next
number in a Fibonacci sequence is defined as the sum of the previous two
numbers, and the first two numbers are defined as 0 and 1, respectively.

'

"""

def fib(n):
    final=[0,1]
    for i in range(n):
        if i>1:
            final.append(final[i-2]+final[i-1])
    return final[:n]