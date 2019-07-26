"""'

Write a recursive Python function `rec_sum_digits(n)', ' that returns the sum
of the digits of an integer number.

'

"""

def rec_sum_digits(n):
    if n<10:
        return n
    else:
        return (n%10)+rec_sum_digits(n//10)