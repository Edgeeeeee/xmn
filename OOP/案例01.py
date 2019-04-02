'''
定义一个类，形容学生
'''
class Student():
    # 一个空类，pass表示直接跳过
    pass
mingyue = Student()


class PythonStudent():
    name = None  # 用给不确定的值赋值
    age = 8
    course = "python"

    def doHomework(self):
        # 注意def的缩进层级
        # 系统默认有一个self参数
        print("i iam learning")
        # 推荐在末尾使用return None
        return None

yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.course)
yueyue.doHomework()
# 注意成员函数的调用没有传递进入参数

