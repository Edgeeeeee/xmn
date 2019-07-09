# JSON
- 在线工具
    - [传送门1](https://www.sojson.com)
    - [传送门2](http://www.w3school.com.cn/json/)
    - [传送门3](http://www.runoob.com/json/json-tutorial.html)
- JSON(JavaScriptObjectNotation)
- 轻量级的数据交换格式，基于ECMAScript
- json格式是一个键值对形式的数据集
    - key：字符串
    - value：字符串，数字，列表，json
    - json使用大括号包裹
    - 键值对之间用大括号隔开
            
            stduent={
                "name":"xmn",
                "age":"18,
                "mobile":"18845163129"
                }
                
- json和Python格式的对应
    - 字符串：字符串
    - 数字：数字
    - 队列：list
    - 对象：dict
    - 布尔值：布尔值
    
- python for json
    - json包
    - json和python的转换
        - json.dumps():对数据编码，把python格式表示成json格式
        - json.loads():对数据解码，把json格式表示成python格式
    - python读取json文件
        - json.dump():把内容写入文件
        - json.load():把json文件写入python