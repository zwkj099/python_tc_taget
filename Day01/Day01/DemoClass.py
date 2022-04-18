# -*- coding: utf-8 -*-
# @Time :2022/4/14  20:31
# @Auther:Huwen
# @File:DemoClass.py


class Person(object):
    pass

    def __init__(self, name, age, sex, area):
        self.name = name
        self.age = age
        self.sex = sex
        self.area =area
        x = Person("www", "22", 'boy', 'cq')
        print(x.name)
        print(x.age)
        print(x.sex)
        print(x.area)


# class Animal(object):
#     pass
#     localtion = 'Asia'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         dog = Animal('wangwang', 1)
#         cat = Animal('mimi', 3)
#         print(dog.localtion)  # ==> Asia
#         print(cat.localtion)  # ==> Asia
#         # 类属性，也可以通过类名直接访问
#         print(Animal.localtion)  # ==> Asia
