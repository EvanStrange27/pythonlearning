# -*- coding: utf-8 -*-

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax^2 + bx + c = 0
#的两个解。
#提示：计算平方根可以调用math.sqrt()函数

import math

def quadratic(a, b, c):
    d = math.sqrt(b*b - 4*a*c)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return x1, x2