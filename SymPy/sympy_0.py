"""
Program could be runned in isympy context for interacrtive

展开 e^(i*x)
"""
from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()

def Expand_E():
    # return expand(E**(I*x), complex = True)
    # 将x指定为实数,需要重新定义x,加入参数real
    x = Symbol("x", real = True)
    return expand(E**(I*x), complex = True)

def Taylor_Expand():
    # 在x=0处进行Taylor展开
    tmp = series(exp(I*x), x, 0, 10)
    return tmp

import numpy as np
def latex_E():
    # 在python中使用Latex,将表达式转为Latex格式
    return latex(exp(I*x+cos(x)))


def main():
    ex_num = Expand_E()
    print(ex_num)
    print(Taylor_Expand())
    print(latex_E())

if __name__ == "__main__":
    main()