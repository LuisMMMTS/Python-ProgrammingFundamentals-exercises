"""'

Write a Python function `no_consecutives1(k)', ' that, given an integer `k',
', determines the number of binary numbers of length `k', ' that do not have
consecutive 1s in them.

'

"""

def no_consecutives1(k):
    lst=[]
    final_lst=[]
    for i in range(2**(k)):
        lst.append(bin(i)[2:])
    for i in lst:
        consecutive=False
        for j in range(1,len(i)):
            if i[j]=="1" and i[j-1]=="1":
                consecutive=True
        if not consecutive:
            final_lst.append(i)
    return len(final_lst)