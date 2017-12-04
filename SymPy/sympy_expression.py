# coding:utf-8

from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()

"""
Sympy中的数学表达式
"""

def math_expression():
    var = ("x0,y0,x1,y1")
    return var

def _is_attr():
    x = symbols('x', positive=True)
    print(x.is_Symbol)
    print(x.is_positive)
    print(x.is_imaginary)
    print(x.is_complex)
    # 使用x.assumptions0来查看所有的假设条件
    print(x.assumptions0)
    # 在Sympy中，所有的对象都是从Basic中继承

def Sympy_data_obj():
    # Sympy中的数值对象，S对象
    # res为Rational对象
    res = (S(1)/2 + S(2)/3)
    return res

# 查看数字的有效位数下的精度
def Precise_data():
    print(N(0.1, 60))
    # print(N(Real('0.1',60),60))

# Print_expression
# 一个递归操作
def print_expression(e, level = 0):
    spaces = "  "*level
    # 如果e是Symbol或者Number中一个直接输出 return
    if isinstance(e, (Symbol,)):
        print spaces + str(e)
        return
    '''
    DIY by Minux~
    if isinstance(e, (Number,)):
        print spaces + "    " + str(e)
        return
    '''
    if len(e.args) > 0:
        print spaces + e.func.__name__
        for arg in e.args:
            print_expression(arg, level+1)
    else:
        print spaces + e.func.__name__

# 使用Function()创建自定义的数学函数
def custo_function():
    f = Function("f")
    print(f.__base__)
    print(isinstance(f, Function))




if __name__ == '__main__':
    '''
    print(math_expression())
    _is_attr()
    Sympy_data_obj()
    Precise_data()
    print_expression(sqrt(x**2+y**y))
    print_expression(x+3)
    print_expression(x+y)
    '''
    custo_function()