# 结构化文件存储
- xml，json
- 为了解决不同设备之间的信息交换问题
# xml文件
- 参考资料
    - [xml1](https://docs.python.org/3/library/xml.etree.elementtree.html)
    - [xml2](http://www.runoob.com/python/python-xml.html)
    - [xml3](https://blog.csdn.net/seetheworld518/article/details/49535285)
- XML:可扩展标记语言
    - 标记语言：语言中使用尖括号括起来的文本字符串标记
    - 可扩展：用户可以自己定义需要的标记
    - 例如：
            
            <Teacher>
                自定义标记Teacher
                在两个标记之间的内容都应该根teacher相关
            </Teacher>
            
    - 是w3c组织指定的一个标准
    - XML描述的是数据本身，及数据的节构和语义
    - HTML侧重于如何显示web页面中的数据
    
- XNL文档的构成
    - 处理指令（可以认为一个文件只有一个处理指令）
        - 最多只有一行
        - 必须在第一行
        - 内容是与XML本身处理相关的一些声明或者指令
        - 以xml关键字开头
        - 一般用于声明xml的版本和采用的编码
            - version属性是必修的
            - encoding实行用来支出xml解释器使用的编码
        - <?xml version="1.0" encoding="utf-8">  直接抄下来就行了。。。
    - 根元素（一个文件内只有一个根元素）
        - 在整个xml文件中，可以把它看作一个树形结构
        - 根元素有且只能有一个
    - 子元素
    - 属性
    - 内容
        - 表明标签所存储的信息
    - 注释
        - 起说明作用的信息。
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释的开头而不能用在结尾
        
                <name> <!-- 注释 --> </name>  # 可以
                <name <!-- 注释 -->> </name>  # 不可以 不能再标签中
                
                <!-- 注释1-注释2-注释3 -->  # 可以
                <!-- 注释1 -- 注释2 -- 注释3 --> 不可以 双短横线只能在开头和结尾
                
                <!--- 注释1 -->  # 可以
                <!--- 注释1 --->  # 不可以 三短横线只能在开头。
                
- 保留字符的处理
    - XML中使用的符号可能跟实际符号相冲突，典型的就是左右尖括号
    - 使用实体引用(EntityReference)来保留字符
    - 可以理解为转义字符。
    
            <score> score>90 </score>  # 错误，内容中不能出现‘<’
            <score> score&gt;90 </score>  # 使用实体引用。
            
    - 把含有保留字符的部分放在CDATA块内部，CDATA巴内部信息视为不需要转义
            
            <![CDATA[
                SELECT NAME,AGE
                FROM STUDENT
                WHERE SCORE > 90
                ]]>
    
    - 常用的需要转义的保留字符和对应的实体引用。
        - &：&amp；
        - <：&lt；
        - >：&gt；
        - '：&aops；
        - "：&quot；
                
- XML标签的命名规则
    - Pascal命名法
    - 用单词表示，第一个字母大写
    - 大小写严格区分
    - 配对的标签必须一直
    
- 命名空间
    - 归并两个内容信息，可能会产生冲突
    - 为了防止命名冲突，需要给可能冲突的元素添加命名空间
    - xmlns：xml name space
    
        <Schooler xmlns:student="http://my_student" xmlna:room="http://my_room">
            <student:Name> xmn </student:Name>
            <room:Name> 十公寓 </room:Name>
            <age> 19 </age>
        </Schooler>
        
        
# XML访问
## 读取
- XML读取分为两个主要技术，SAX,DOM
- SAX（simple API for XML)
    - 基于事件驱动
    - 利用SAX解析文档涉及到解析器和事件处理两部分
    - 特点
        - 块
        - 流式读取
        
        
- DOM
    - 是W3C规定的XML编程接口
    - 一个XML文件在缓存中以树形结构保存，读取 
    - 用途：
        - 定位浏览XML任何一个结点信息
        - 添加删除相应内容。
    - minidom
        - minidom.parse(filename):加载读取的XML文件，filename也可以是xml代码
        - doc.documentElement:获取XML文档，一个XML文件只有一个对应的SML文档对象
        - node.getAttribute(attr_name):获取XML结点的属性值
        - node.gerElementByTagName(tage_name):得到一个节点对象集合
        - node.childNodes:得到所有孩子结点
        - node.childNodes\[index].nodeValue:获取单个结点值
        - node.firstNode:得到第一个结点，等价于node.childNodes\[0]
        - node.attribute\[tage_name]
    - etree
        - 以树形结构来表示XML
        - root.getiterator：得到相应的可迭代的node集合
        - root.iter
        - find(node_name):查找指定node_name的结点
        - root.findall(node_name):返回多个node_name的结点
        - node.text:node的文本文档
        - node.attrib:是node的属性的字典类型的内容。
        - node.tag：node对应的tagename
        
## 写入
- 更改
    - ele.set:修改属性
    - ele.append:添加子元素
    - ele.remove:删除元素
- 生成创建（常用）
    - SubElement(ele,"name") 生成ele元素的子元素。
    - dump(ele)  生成一个xml文件，根节点为ele
    - minidom写入
    - etree写入


