#coding:utf-8

from __future__ import division
from sympy import *
x, y, z = symbols('x y z')

"""
在Symbol中可以直接表示值为0的方程，也可以使用Eq()创建方程，solve()
可以直接对方程进行求解
"""
a, b, c = symbols('a b c')

def solve_equation():
    return solve(a*x**2+b*x+c, x)

# 对方程组进行求解
def solve_equation_coup():
    return solve((x**2+x*y+1,y**2+x*y+2),x,y)

# 对函数进行微分
def derivative_func():
    # 实际运算计算出导函数，需要调用doit()方法
    return Derivative(x**2+sin(x),x).doit()
def derivative_func_eq():
    # 计算导函数的等效方法
    return diff(x**2+sin(x), x)
def derivative_func_mul():
    return diff(sin(x*y),x,2,y,3)

if __name__ == '__main__':
    print(solve_equation())
    print(solve_equation_coup())
    print(derivative_func())
    print(derivative_func_eq())
    print(derivative_func_mul())