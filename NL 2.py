import math
import sympy as sp
import numpy as np
from sympy import *

x = sp.symbols('x')
fun = [] ## Differentiated functions list
rms = [1] ## Newton Raphson trial result storage lists
rms2 = []
rms3 = []
rms4 = []

rms5 = [] ##Inflection points lists
rms6 = []

key = 0

max = int(input('최고차수를 입력하세요: '))
f_x = sp.expand(input('함수를 입력하세요: '))


fun.append(f_x)
while max >0:
    fun.append(sp.diff(f_x))
    f_x = sp.diff(f_x)
    max = max -1
f_x = fun[0]

n = len(fun)

while n >= 1:
    if float(fun[n-1].subs(x,0)) == 0:
        del fun[n-1]
        n = n - 1
    else:
        break

n = len(fun)
print(fun)

while n > 1:
    if n == 2 and len(rms) == 0:
        rms.append(1)
    if key == 1:
        rms.extend(rms6)
        rms6.clear()
    elif key == 2:
        rms.extend(rms5)
        rms5.clear()
    else:
        pass
    k = len(rms)
    while k >= 1:
        x_1 = rms[k-1]
        i = 0
        while i <= 10000:
            if float(fun[n-1].subs(x,x_1)) == 0:
                break
            else:
                x_2 = float(x_1) - float(fun[n-2].subs(x,x_1))/float(fun[n-1].subs(x,x_1))
                x_1 = round(x_1, 10)
                x_2 = round(x_2, 10)
                if x_2 == x_1:
                    break
                else:
                    x_1 = x_2
                    i = i + 1
        if i == 10001:
            k = k - 1

        elif float(fun[n-1].subs(x,x_1)) == 0:
            k = k - 1

        else:
            x_2 = np.trunc(x_2 * 10000000000) / 10000000000
            rms2.append(x_2)
            k = k - 1
    if len(rms2) == 1 and n == len(fun):
        rms5 = rms2.copy()
        rms2.append(rms2[0] + 1)
        rms2.append(rms2[0] - 1)
        rms2.sort()
        del rms2[1]
        rms = rms2.copy()
        rms2.clear()
        n = n - 1
    elif len(rms2) > 1:
        for v in rms2:
            if v not in rms4:
                rms4.append(v)
        rms2 = rms4.copy()
        rms2.sort()
        if len(rms5) == 0:
            rms5 = rms2.copy()
            key = 1
        else: #len(rms6) ==0
            rms6 = rms2.copy()
            key = 2

        if n == 2:
            n = n - 1
            break
        else:
            rms3.append(rms2[0] - 10)
            rms3.append(rms2[-1] + 10)
            a = 0
            while a < len(rms2) - 1:
                rms3.append((rms2[a] + rms2[a+1]) / 2)
                a = a + 1
            rms3.sort()
            rms = rms3.copy()
            rms2.clear()
            rms3.clear()
            rms4.clear()
            n = n - 1
    else:
        n = n - 1
if len(rms2) == 0:
    print("해가 존재하지 않습니다.")
else:
    print("함수의 실근:")
    print(rms2)

plot(f_x,xlim=(-1000,1000),ylim=(-1000,1000)) ## Drawing graph for checking correct answer.

