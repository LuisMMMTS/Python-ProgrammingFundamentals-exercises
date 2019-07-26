"""'

Define a function called `hypotenuse(n)', ' that given the length `n', ' which
corresponds to two sides of a right-angled triangle, it returns the length of
the hypotenuse. Please use round with two decimal places.

'

"""

def hypotenuse(n):
	 n=2*(n**2)
	 return round(n**(1/2),2)