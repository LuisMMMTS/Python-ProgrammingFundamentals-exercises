"""'

Write a Python function `sort_by_key(dict)', ' that, given a dictionary
`dict', ' of colors (key is the color name and value is its hexadecimal
value), returns a list of pairs ordered by color. Note that It is not possible
to sort a dictionary, only to get a representation of a dictionary that is
sorted.

'

"""

def sort_by_key(dict):
	 l=[]
	 for key,value in dict.items():
	 	 l.append((key,value))
	 return sorted(l)