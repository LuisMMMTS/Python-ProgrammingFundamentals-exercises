"""'

Write a Python function `dogs(h_age)', ' that receives the dog’s age in human
years `h_age', " and returns the corresponding dog's age in dog's years. For
the first two years, a dog year is equal to 10.5 human years. After that, each
dog year equals 4 human years.

"

"""

def dogs(h_age):
    d_age=0
    for i in range(2):
        if h_age>0:
            h_age-=1
            d_age+=10.5
    if h_age>0:
        d_age+=h_age*4
    return d_age

print(dogs(5))