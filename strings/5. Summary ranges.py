"""'

Given a comma-separated string `astring', ' with sorted integers without
duplicates, write a Python function `summary_ranges(astring)', ' that returns
a string showing the contiguous intervals in the set.

'

"""

def summary_ranges(astring):
    astring=astring.split(",")
    mem=astring[0]
    mem2=mem
    out=""

    for i in range(1,len(astring)):
        if int(mem2)+1==int(astring[i]) and i!=len(astring)-1:
            mem2=astring[i]
            continue
        
        elif i==len(astring)-1:
                if int(mem2)+1==int(astring[i]):
                    out+=","+mem+"->"+astring[i]
                else:
                    if mem==astring[i-1]:
                        out+=","+mem+","+astring[i]
                    else:
                        out+=","+mem+"->"+astring[i-1]+","+astring[i]
                
        else:
            if mem==astring[i-1]:
                out+=","+mem
            else:
                out+=","+mem+"->"+astring[i-1]
            mem=astring[i]
            mem2=mem
    
    out=out[1:]
        
    return out
