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

def expand_cos():
    # 对cos(x)进行Taylor展开对比exp(i*x)
    cos_e = series(cos(x), x, 0, 10)
    com_e = series(exp(I*x), x, 0, 10)
    print(re(com_e))
    print(im(com_e))
    return cos_e

# SymPy中进行不定积分运算
def integrate_E():
    return integrate(x*sin(x), x)

# 通过定积分得到半圆的面积
def semi_circle():
    # 定义运算符号
    x, y, r = symbols('x, y, r')
    # 这里直接返回了原表达式，因为不知道r的正负关系
    temp = 2*integrate(sqrt(r**2-x**2), (x, -r, r))
    # 对r进行重新定义
    r = symbols('r', positive=True)
    circle_area = 2 * integrate(sqrt(r**2-x**2), (x, -r, r))
    # 对circle_area进行定积分就可以得到球的体积
    # 利用subs特性进行替换
    circle_area = circle_area.subs(r, sqrt(r**2-x**2))
    # 对circle_area在-r到r区间上进行定积分
    return integrate(circle_area,(x, -r, r))

# 测试Latex中的功能
import numpy as np
def latex_E():
    # 在python中使用Latex,将表达式转为Latex格式
    return latex(exp(I*x+cos(x)))

def main():
    ex_num = Expand_E()
    # print(ex_num)
    # print(Taylor_Expand())
    # print(latex_E())
    # print(expand_cos())
    # print(integrate_E())
    print(semi_circle())

if __name__ == "__main__":
    main()