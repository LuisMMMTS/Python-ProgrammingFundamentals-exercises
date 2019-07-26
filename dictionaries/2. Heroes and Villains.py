"""'

Write a Python function `fight(heroes, villain)', ' that, given a list of
`heroes', ' and a `villain', ', checks if the good side can prevail. Each hero
in the list has a set of properties stored in a dictionary: name, health,
category and score (number of victories). The villain has a similar structure,
but does not record his score. The fight occurs within the following set of
restrictions:

'

"""

def fight(heroes, villain):
    for i in heroes:
        if i["category"]!=villain["category"]:
            continue
        elif villain["health"]>0 and i["name"]==heroes[-1]["name"] and
villain["health"]>i["health"]:
            return villain["name"]+" prevailed with
"+str(villain["health"]-i["health"]/2)+"HP left"
            
        else:
            if i["health"]>=villain["health"]:
                i["score"]+=1
                return i["name"]+" defeated the villain and now has a score of "\+
str(i["score"])
                
            else:
                villain["health"]-=i["health"]/2
