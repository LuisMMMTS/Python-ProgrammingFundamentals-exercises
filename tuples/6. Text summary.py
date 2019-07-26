"""'

Given a text -- perhaps a poem, a speech, instructions to bake a cake, some
inspirational verses, etc. -- write a function called `summary(text)', ' that
given a string `text', ', returns a tuple with the number of total words, and
the number of words that contain at least an "e" (upper or lower case).

'

"""

def summary(text):
    text=text.lower()
    palavras,n_e=0,0
    for i in text.split():
        palavras+=1
        if "e" in i:
            n_e+=1
    return (palavras,n_e)
