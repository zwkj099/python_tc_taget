#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time :2022/4/16  17:01
# @Auther:Hu wen
# @File:DataType.py


"""
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）


"""
#多个变量赋值
a, b, c, d = 20, 5.5, True, 4+3j
#d,e,f=1,2,3
print(a,b,c,d)

class A:
    pass
class B:
    pass

"""
isinstance 和 type 的区别在于：

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""
print(isinstance(A(),A))
