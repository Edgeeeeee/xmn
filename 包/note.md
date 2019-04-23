# 1. 模块
- 一个模块就是一个包含python代码的文件，后缀名是,py就可以，模块就是一个python文件
- 为什么要用模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当作命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，任何代码可以直接书写。
    - 不过根据模块的规范，最好在模块中编写以下内容
        - 函数(单一功能)  （高内聚，低耦合）
        - 类(相似功能的组合，或者类似业务模块)
        - 测试代码（便于别人修改，扩展后测试，方便别人用的）
- 如何使用模块
    - 模块直接导入
        - 加入模块名称直接以数字开头，借助于importlib包可以实现导入
        - 举例：xmn = importlib.import_module("01")  # 01 为模块名称，xmn为模块的别名
        - 或者模块的名字比较长： import 模块 as 别名
    - 语法
    -       导入:import module_name
            使用：module_name.function_name
                  module_name.class_name
                          
        - 所谓的导入相当于把代码直接粘过来
    - form module_name import func_name,class_name
        - 从模块中有选择性导入部分功能
        - 导入后不需要用前缀了，直接写函数或者类即可，写多会报错。
        - 避免了代码的冗余 
    - from module_name import *
        - 导入模块所有东西
        - 利：省事了，不用写前缀
        - 弊：防止不了命名污染了
        
    - if \_\_name\_\_ = '\_\_main__': 的意思是
        - 当此文件是自己调用的时候执行if下的语句  此时 \_\_name__ = __main__
        - 当此文件是被其他文件调用的时候，\_\_name__ 为调用此文件的文件名字，则if块下的语句不会执行
        - __此判断语句建议一直作为程序的入口__
        - 可以有效避免模块代码被导入的时候被动执行的问题
        
# 2.模块的搜索路径和存储
- 什么是模块的搜索路径：
    - 加载模块的时候，系统会在那些地方寻找此模块
- 系统默认的模块搜索路径
-
    import sys
    sys.path 属性可以获得所有被搜索的路径的列表
    for i in sys.path:
        print(i)
    
- 此代码可以打出所有查找路径
- 添加路径  sys.path.append(dir)  dir 为字串格式
- 模块的加载顺序
    - 1. 搜索内存中已经加载好的模块
    - 2. 搜索python的内置模块
    - 3. 搜索sys.path路径 按list顺序   
    
    
# 包
- 包是一种组织管理代码的方式，__包里面存放的是模块__
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构
- 
        |---包
        |---|---__init__.py  包的标志性文件
        |---|--- 模块1
        |---|--- 模块2
        |---|---子包（子文件夹）
        |---|---|---__init__.py   标志文件
        |---|---|---子包模块1
        |---|---|---子包模块2
        
- 结构与普通文件夹大致相同 就是文件夹里必须要有一个\_\_init__.py 标志文件
- 包的导入操作
    - import package_name 
        - 直接导入一个包，可以使用\_\_init__.py里的内容
        - 使用方式是：
        -
                package_name.func_name
                package_name.class_name
              
        - 此种方式的访问内容是 只能使用\_\_init__里的内容，但是一般\_\_init__.py里都是空的
    
    - import package as p: 此方式与上面的一样，只导入了\_\_init__.py 文件，只是用了个别名
    - import package.module
        - 导入包中某一个具体的模块。
        - 使用方法
        -
                package.module.func_name
                package.module.dlass.fun()
                package.module.class.var
                
    - import package.module as pm 
        - 与之前一样，写pm前缀
        
    - from ... import ...导入
        - from package import module1,module2
        - 此种方法不执行\_\_init__.py 的内容，写模块名前缀
        
        - from package import *
            - 导入 \_\_init__.py ' 文件中的所有函数和类，不用写前缀
           
        - from package.module import *
            - 导入包中指定的模块的所有的内容，不用写前缀           
    - 在开发环境中经常会引用其他模块，可以在当前包中直接导入其他模块的内容
        - import 完整的包或者模块的路径（符合系统的路径）                
    - \_\_all__用法 （这不是一个函数）
        - 在使用from package import * 的时候， *可以导入的内容
        - 在\_\_init__.py 中如果文件为空，或者没有\_\_all__ 的时候，那么只可以把` __init__`  中的内容导入
        - 如果在`__init__.py` 中设置了`__all__`的值 则会按照`__all__`指定的子包或者模块进行加载
        - 如此则不会导入`__init__`中的内容
        - 例如：`__all__ = \['module1','module2','package1',...]
        
        
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的特定前缀
- 作用是防止命名冲突