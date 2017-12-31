# coding:utf-8

from __future__ import division
from sympy import *
from sympy.geometry import *

a = symbols("a", positive=True)

def geometry_point():
    A = Point(0, 0)
    B = Point(5, 0)
    C = Point(3, 2)


    t = Triangle(A, B, C)
    # D为三角形的内切圆的圆心
    D = t.incenter
    print(D)
    # 通过圆上的三点创建圆形
    p = Circle(C, D, B)
    print(p)


    i = Segment(*p.intersection(Line(A, B)))
    j = Segment(*p.interseciton(Line(A, C)))

    print i.length.evalf(50)
    print j.length.evalf(50)

if __name__ == '__main__':
    geometry_point()
