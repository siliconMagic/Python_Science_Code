# coding:utf-8

from __future__ import division
from sympy import *


x, y, z, a, b = symbols('x y z a b')

f, g, h = symbols('f g h', cls = Function)
"""
利用integrate()计算定积分和不定积分
"""

def calc_integrate():
    e = Integral(x*sin(x), x)
    return e.doit()

# 对有些积分可以进行化简
def evalf_integrate():
    e = Integral(sin(x)/x, (x, 0,1))
    return e.evalf()

# 计算无限范围定积分
def calc_unlimit():
    # oo表示正无穷，将上限改成1000可以计算出PI/2的近似值
    return N(Integral(sin(x)/x,(x,0,1000)))

# 将定积分转换为近似的求和公式
def integral_sum():
    return Integral(sin(x), (x, 0, 1)).as_sum(10)

if __name__ == '__main__':
    print(calc_integrate())
    print(evalf_integrate())
    # print(calc_unlimit())
    print(integral_sum())