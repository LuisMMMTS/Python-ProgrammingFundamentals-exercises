"""'

Write a Python function `collatz(n)', ' that returns a comma-separated string
with the Collatz sequence. Starting by the positive integer `n', ', the next
term of the Collatz sequence is obtained from the previous by: (i) diving the
previous term by 2, if the previous term is even; or (ii) multiplying the
previous term by 3 and then summing 1, if the previous term is odd. The
sequence ends when it reaches 1.

'

"""

def collatz(n):
    string=[]
    while n!=1:
        string.append(int(n))
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
    string.append(1)
    string=str(string)[1:-1]
    return string.replace(" ","")
