"""'

Write a Python function `interleave(f1, f2)', ' to combine each line from
first file (`f1', ') with the corresponding line in second file (`f2', "),
while there's lines in both files.

"

"""

def interleave(f1, f2):
    f1=open (f1,"r")
    f2=open (f2,"r")
    s=""
    l1=f1.readlines()
    l2=f2.readlines()
    for i in range(min(len(l1),len(l2))):
       s=s+str(l1[i])
       s=s+str(l2[i])
    return s