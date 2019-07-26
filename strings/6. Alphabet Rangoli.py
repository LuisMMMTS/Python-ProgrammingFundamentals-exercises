"""'

Given an user-defined integer `N', ', write a Python function `rangoli(N)', '
to return an alphabet rangoli of size `N', '. (Rangoli is a form of Indian
folk art based on creation of patterns.)

'

"""

def rangoli(N):
   summary=[]
   rang=""
   
   for i in range(1,N+1):
       summary.append(line_construct(i*2+1,N))
       
   a=len(max(summary, key=len))

   for i in summary:
       b=((a-len(i))//2)
       rang=rang+"-"*b+i+"-"*b+"\n"
   rang=rang[:-a-2]+rang[::-1]
   return rang
       
   
        
       
def line_construct(line_len,N):
    #line construction
    line=""
    line2=""
    for i in range(line_len//2):
        line=line+chr(96+N-i)
    line=line[::1]+line[-2::-1]
    for i in line:
        line2=line2+i+"-"
    return line2[:-1:]