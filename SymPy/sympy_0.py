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
    return expand(E**(I*x), complex = True)

def main():
    ex_num = Expand_E()
    print(ex_num)

if __name__ == "__main__":
    main()