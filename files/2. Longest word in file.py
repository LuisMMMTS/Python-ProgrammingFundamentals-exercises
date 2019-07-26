"""'

Write a Python function `longest(filename)', ' that given the string
`filename', ' returns the longest word in the text file.

'

"""

def longest(filename):
	 f=open(filename,"r")
	 lines=f.readlines()
	 lines=str(lines)
	 return(max(lines.replace("'","").split(" "),key=lambda x:len(x)))
    