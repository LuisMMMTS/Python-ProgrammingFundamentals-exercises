"""'

Write a Python function `palindrome_index(s)', ' that, given a string `s', ',
returns the index of the first character that, if removed, turns the string
into a palindrome. If there is no such character or the string already is a
palindrome, it should return `-1', '.

'

"""

def palindrome_index(s):
    new_string=""
    index=-1
    if s==s[::-1]:
        index=-1
    else:
        for a in range(len(s)+1):
            new_string=s[:a]+s[a+1:]
            if new_string==new_string[::-1]:
                index=a
                break
    return index
