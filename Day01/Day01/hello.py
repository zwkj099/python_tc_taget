#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time :2022/4/15  9:40
# @Auther:Hu wen
# @File:hello.py




import sys;
x = 'runoob'; sys.stdout.write(x + '\n')


print("hello,world")
"""


dd 
dfsd
"""
if True:
    print("你是个傻子")
else:
    print("你不是")

str="dasljdaklsjdlkashl \n dkha0003042423 \n"
str1=r"dasljdaklsjdlkash \n dkha0003042423 \n" #字符前缀加上r 表示不转义
print(str[1])  #正向索引 ，字符串取值通过索引取   方式  字符串标识符 [索引id]
print(str[-1])  #反向索引  索引id负数
print(str)
print(str1)

#字符串自动级联
str3="yyy""rrrr"

str4="123456789"
print(str3)
print(len(str3))  #计算字符的长度
print(type(str3)) #判断值的类型
print(str * 2) #输出两遍字符
print(str4[1:5:2])

input("\n\n 按下Enter")


