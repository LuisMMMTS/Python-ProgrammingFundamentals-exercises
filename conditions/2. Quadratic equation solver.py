"""'

Define a function `solver(a, b, c)', ' that returns the solution to the
quadratic formula of the type: ax²+bx+c=0. Return the result in the form of a
list: empty list if no solution exists in ℝ, a list with one or two elements
if one or two solutions exist, respectively; if there are two solutions, use
ascending order.

'

"""

import math
def solver(a,b,c):
    root=[]
    if ((b**2)-4*a*c)>0 or (((b**2)-4*a*c)==0 and b==0):
        root.append((-b+math.sqrt((b**2)-4*a*c))/(2*a))
        if (-b-math.sqrt((b**2)-4*a*c))/(2*a)!=(-b+math.sqrt((b**2)-4*a*c))/(2*a):
            root.append((-b-math.sqrt((b**2)-4*a*c))/(2*a))
            root.sort()
    return root

print(solver(1,-3,7))