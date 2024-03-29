import sympy as sp

x = sp.var('x')

def dev(coeffs):
    [b,c,d,e,f,g,h,i,j] = coeffs
    expr = ((b*x+c)*(d*x+e)+f*(g*x+h)*(i*x+j))
    return latex(expr.expand())

EXO1=[
[5,-1,-3,-9,-5,-10,-2,-10,-5],
[-1,1,7,-1,-7,-2,-3,6,-8],
[-1,0,-9,1,8,10,1,5,-9],
[0,-4,-10,-3,2,7,-10,6,3],
[-9,-4,0,0,8,3,9,-8,-9],
[-10,-5,-1,-4,2,3,2,-4,4],
[7,3,-10,-8,-1,-8,-10,8,10],
[-10,9,8,10,9,7,4,8,-7],
[-6,3,6,0,-9,-5,-5,0,-10],
[-7,-10,-2,0,-6,6,-1,-5,-1],
[8,6,10,8,-9,-1,-5,0,3],
[-4,10,5,1,-8,10,-8,-3,-7],
[-8,-9,-6,5,-6,-6,-1,5,-5],
[2,-4,5,7,5,-5,0,-2,2],
[1,-4,2,2,6,6,6,1,-9],
[-5,-9,0,-7,-8,-3,8,3,3],
[10,-9,-9,-7,9,-1,4,7,8],
[10,-6,-1,1,-9,0,-3,0,1],
[7,9,-3,-8,-1,4,-3,6,-10],
[-10,0,8,10,3,-6,-8,2,0],
[5,-10,0,-6,-9,5,4,-4,2],
[-6,6,3,0,-8,-9,-5,-10,4],
[10,8,-9,5,-9,1,3,-8,-6],
[-6,7,9,7,-7,0,10,9,7],
[3,8,3,10,-3,-1,-1,-10,-2],
[7,-2,-8,-6,9,-10,-3,9,-1],
[7,9,8,5,1,-10,-1,-2,-7],
[9,7,3,-7,6,-9,9,-8,-2],
[5,-9,-3,3,9,2,6,6,6],
[-3,4,-6,2,7,4,8,3,4],
[2,-8,2,6,-5,-3,2,2,-9],
[4,-9,3,-2,8,1,10,8,10],
[1,8,4,-7,-1,-10,-7,2,0],
[0,0,-7,-4,-2,-5,7,9,2],
[-7,5,1,2,-4,1,-7,-10,-10],
[0,-7,2,-6,4,10,3,2,-10],
[8,2,0,0,-1,-9,10,-10,0],
[10,0,4,7,-1,7,-4,10,4],
[10,-10,5,0,4,3,-10,-2,7],
[-1,8,-4,-9,1,6,0,0,-1]
]

k = 0
for case in EXO1:
    k += 1
    print(k,':',dev(case))
