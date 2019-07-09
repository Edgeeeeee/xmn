# 包含一个学生类
# 一个sayhello函数
# 一个打印语句
import pymysql
class Student():
    def __init__(self,name = "noname",age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayhello():
    print("Hi,guys!")

print("p01是一个模块。。。。。。。。。  最好不要写在模块中写这种函数")
# 在p02中调用