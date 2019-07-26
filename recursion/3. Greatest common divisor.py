"""'

Write a recursive Python function `rec_gcd(n1, n2)', ' to find the greatest
common divisor ( _gcd_ ) of two integers `n1', ' and `n2', '.

'

"""

def rec_gcd(n1,n2):
	 if n2==0:
	 	 return n1
	 return rec_gcd(n2,n1%n2)