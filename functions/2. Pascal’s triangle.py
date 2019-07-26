"""'

Write a Python function `pascal(n)', ' that, for a given integer `n', ',
returns a string with the first `n', ' rows of the Pascal\'s triangle. Each
row finishes by `"\\\n"', ' (newline) and each value is separated by a single
space. The value at the _i_ -th row and _j_ -th column of the triangle is
equal to _i!/(j!*(i-j)!)_. Note: _i_ and _j_ start in zero.

'

"""

from math import factorial as fact
def pascal (n):
    string=""
    for linhas in range(0,n):
        for colunas in range(0,linhas+1):
            string+=(str(int((fact(linhas))/((fact(colunas))*(fact(linhas-colunas)))))+"
")
        string+=("\n")
    return string