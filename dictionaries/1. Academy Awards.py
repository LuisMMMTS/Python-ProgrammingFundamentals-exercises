"""'

Write a Python function `academy_awards(alist)', ' which receives a list of
tuples, `alist', ', where each tuple holds the category and the corresponding
winning movie and returns a dictionary that maps each movie to the number of
awards that it won.

'

"""

def academy_awards(alist):
    awards={}
    for i,j in alist:
        if j not in awards.keys():
            awards[j]=1
        else:
            awards[j]+=1
    return awards
