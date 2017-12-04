#coding:utf-8

from __future__ import division
from sympy import *
x, y, f, z = symbols('x, y, f, z')

def simply_func():
    return simplify((x+2)**2 - (x+1)**2)

def return_fraction():
    # 将分子和分母组成tuple返回
    return fraction(ratsimp(1/x+1/y))

# 使用trigsimpl_function()函数进行化简
def trigsimp_function():
    #return trigsimp(sin(x)**2+2*sin(x)*cos(x)+cos(x)**2)
    return trigsimp(f(sin(x) ** 2 + 2 * sin(x) * cos(x) + cos(x) ** 2), deep=True)

# 使用expand_trig将表达式展开
def expand_trig_function():
    return expand_trig(f(sin(x+y)*(x-y)))

# 展开加法等式的表达式乘积
def expand_multi_nomminal():
    return expand((x+y)**3)

# 展开幂函数的指数和
def expand_M():
    return expand(x**(y+z))

# 展开一些特殊函数
def expand_special_function():
    return expand(gamma(1+x), func=True)

# 展开三角函数
def expand_trig_func():
    return expand(sin(x+y), trig=True)

# factor对多项式进行因式分解
def factor_func():
    return factor(15*x**2+2*y-3*x-10*x*y)

f, g, h = symbols('f g h', cls=Function)
k, m, n, a, b = symbols('k m n a b', integer=True)

# 使用collect()收集各幂的次数, 将参数evalute的参数设置为False,
# 返回一个以x的幂为键，值为系数的字典
def collect_func():
    eq = (1+k*x)**3
    eq_2 = expand(eq)
    p = collect(eq_2, x, evaluate=False)
    print p[S(1)]
    print p[x**2]
    return p

# collect()可以收集指定项的系数
def collect_func_x():
    p = collect(a*sin(2*x)+b*sin(2*x), sin(2*x))
    return p

if __name__ == '__main__':
    print(simply_func())
    print(return_fraction())
    print(trigsimp_function())
    print expand_trig_function()
    print expand_multi_nomminal()
    print expand_M()
    print(expand_special_function())
    print(expand_trig_func())
    print(factor_func())
    print(collect_func())
    print(collect_func_x())