#coding:utf-8

from __future__ import division
from sympy import *
x, y, z = symbols('x y z')
f = Function("f")
def d_solve():
    return dsolve(Derivative(f(x), x) - f(x), f(x))

x = symbols("x", real = True)
def solve_function():
    # best参数会尝试所有的解法
    eq1 = dsolve(f(x).diff(x) + f(x)**2 + f(x), f(x), hint="best")
    return eq1

if __name__ == "__main__":
    print(d_solve())
    # print(solve_function())

