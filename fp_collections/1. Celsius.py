"""'

Write a Python function `to_celsius(t)', ' that, given a list `t', ' of
temperatures in Fahrenheit degrees, uses `map()', ' with a lambda function to
compute the corresponding Celsius degrees, rounded to 1 decimals.

'

"""

def to_celsius(t):
	 t=list(map(lambda x:round((x-32)*5/9,2),t))
	 return t