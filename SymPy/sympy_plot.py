# coding:utf-8

from sympy import *
from sympy.plotting import plot, plot3d, plot3d_parametric_line

def get_plot_2D():
    x = Symbol("x")
    p1 = plot(x/2)
    # print len(p)
    # print p[0]
    p2 = plot(x*x)
    p3 = plot(log(x))
    p1.extend(p2)

def merge_in_pic():
    x = Symbol("x")
    p = plot(x/2, x*x, log(x), (x, -2, 2))

'''
绘制莫比乌斯环
构建参数方程
调用方程plot3d或者plot3d_parametric_line
'''
def draw_complex():
    x, u, v = symbols("x u v")
    x = (1+v/2*cos(u/2)*cos(u))
    y = (1+v/2*cos(u/2)*sin(u))
    z = v/2*sin(u/2)

    # p = plot3d_parametric_line(x, y, z, [u, 0, 2*pi], [v, -1, 1])


if __name__ == "__main__":
    # get_plot_2D()
    # merge_in_pic()
    draw_complex()
