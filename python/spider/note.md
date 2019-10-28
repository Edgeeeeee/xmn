# 准备工作
- 参考资料
    - python网络数据采集。图灵工业出版 
    [Python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    
# 爬虫简介
- 程序或者脚本，自动抓取万维网的信息
- 两大特征
    - 能按作者的要求下载数据或者内容
    - 能自动在网络上流窜
- 三大工作步骤
    - 下载网页
    - 提取正确的信息
    - 根据一定的规则自动跳到另外的网页上执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
- python网络包简介
    - python3.x：urllib，urllib3，httplib2，requests
    - 一般用rullib，requests
   
# urllib
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error：包含urllib.requests产生的常见错误，使用try捕捉
    - urllib.parse：包含解析url的方法
    - urllib.robotparse:解析robots.txt文件
    - 案例v1
    
- 网页编码问题的解决
    - chardet 可以自动检测浏览页面文件的编码格式，但是，可能出错
    - 需要安装 conda install chardet
    - 案例v2
    
- urlopen 的返回对象
    - 案例v3
    - getrul：返回请求对象的url
    - info：请求反馈对象的mete信息
    - getcode：返回的http code
    
- request.data 的使用
    - 访问网络的两种方法
        - get
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
            - 案例v4
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 如果使用post信息，需要用到data参数
            - 使用post，意味着Http的请求头可能需要更改：
                - Contetnt-Type：application/x-www.from-urlencode
                - Content-Length: 数据长度
                - 简而言之，一旦更改请求方法，请注意其他请求头部信息适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的。
            - 案例v5
            - 为了设置更多的请求信息，单纯的urlopen不太好用
            需要利用request.Request类
            - 案例v6
- urllib.error
    - URLError产生的原因
        - 没网
        - 服务器连接失败
        - 找不到指定的服务器
        - 是OSError的子类
- HTTPError
    - 404错误
- 两者的区别
    - HTTPError是对应的HTTP请求的返回错误，如果错误码为400以上为HTTPerror
    - URLError对应一般是网络出现问题，保罗url问题
    - 关系： OSError -> URLError -> HTTPError
    
- UserAgent 
    - UserAgent：用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    
    - 设置UA可以使用两种方式
        - heads
        - add_header
        - 案例v9
        
- Proxyhandler处理（代理服务器）
    - 使用代理IP，是爬虫的常用手段
    - 获取代理服务器的地址:
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许频繁访问一个固定网站，所以代理要很多很多。
    - 代理的基本使用步骤
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建Opener
        4. 安装Opener
    - 案例v10
    
- cookie & session 
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发放给用户（即http浏览器）的一段信息，session是保存在服务器上对应的另一半信息，用来记忆用户信息
    - cookie和session的区别
        - 存放位置不同
        - cookie不安全
        - session会在服务器上保存一段时间，会过期
        - 单个cookie保存数据不会超过4K，很多浏览器限制一个站点最多保存20个（浏览器限制的，不是标准协议限制的，也不是每一个浏览器都限制）
    - session的存放位置
        - 存在服务端
        - 一般情况，session是放在内存中，或者数据库中。
        - 没有cookie登陆，案例v11，反馈网页为未登录状态。
    - 使用cookie登陆
        - 把cookie复制下来，手动放入请求头中。 案例v12
        - http模块包含关于一些cookie的模块，通过他们我们可以自动使用cookie
            - CookieJar
                - 管理存储cookie，向传出的http请求中添加cookie
                - cookie存储在内存中，CookJar回收内存后，cookie会消失
            - FileCookJar(filename, delayload=None, policy=None)
                - 使用文件管理cookie
                - filename是保存cookie的文件
            - MozillaCookieJar(filename, delayload=None, policy=None)
                - 创建与Mozilla浏览器cookie.txt兼容的FileCookJar实例
            - LwpCookJar
                - 创建于libwww-perl标准兼容的Set-Cookie3格式相同的FileCookieJar实例
            - 关系是 CookieJar -> FileCookieJar -> MozillaCookieJar & LwpCookieJar
        - 利用CookieJar访问人人 v13
            - 自动使用cookie登陆 大致流程
            - 打开登陆页面后自动通过用户名密码登陆
            - 自动提取反馈回来的cookie
            - 利用提取的cookie登陆隐私页面
        - handler是Handler的实例，用来处理复杂的请求，常用参看案例代码
        
                # 生成cookie的管理器
                cookie_handler = request.HTTPCookieProcessor(cookie)
                # 生成http管理器
                http_handler = request.HTTPHandler()
                # 生成https管理器
                
        - 创立handler后，使用opener打开，打开后相应的业务由相应的handler处理
        - cookie作为一个变量，打印出来，案例v14
            - cookie的属性
                - name：名称
                - value：值
                - domain：可以访问此cookie的网站
                - path：可以访问此cookie的页面路径
                - expires：过期时间
                - size：大小
                - Http字段
        - cookie的保存-FileCookieJar 案例v15
        - cookie的读取 案例 v16
    - SSL
        - SSL证书就是指遵守SSL安全套接层协议的服务数字证书(SecureSocketLayer)
        - 美国网景公司开发
        - CA(CertificateAuthority)是数字证书认证中心，是发放，管理，废除证书的收信人的第三方机构
        - 遇到不信任的SSL证书，需要单独处理，案例v17
        
    - js加密
        - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是md5值）
        - 经过加密，传输的就是密文，
        - 加密过程一定是在浏览器完成，也就是一定会把代码（js代码）暴漏给使用者
        - 通过阅读加密算法，就可以模拟加密过程，从而破解。
        - 过程 案例v18
    - ajax
        - 异步请求
        - 一定会有url，请求方法，可能有数据
        - 一般使用json格式
        
        
# Requests模块
- HTTP for Humans, 更简洁更友好
- 继承了urllib的所有特征
- 底层使用的使urllib3
- 开源
- 中文文档
- get请求
    - request.get(url)
    - requests.request("get", url)
    - 可以带有headers和parmas参数
    - 案例v21
- get返回内容
    - 案例v22
- post
    - rsp = requests.post(url, data=data, headers)
    - date和headers都用dict 不用编码
- proxy
```python
import requests
proxies = {
"http": "address of proxy",
   "https": "address of proxy"
}
rsp = requests.request("get", "http:xxxx")
```
- 用户验证
     - 代理验证
     
            #可能需要使用HTTP basic Auth
            #格式为 用户名:密码@代理地址:端口
            proxy = {"http":"username:123456@192.168.1.123:5000"}
            rsp = reqeusts.get("http://www.baidu.com", proxies=proxy)
            
- web 客户端验证
    - 如果遇到web客户端验证，需要添加auth=(用户名，密码)
    
            auth = ("account", "123456")
            rsp = requests.get("http://xxxxxx", auth=auth)
        
- cookie
     - requests可以自动处理cookie信息
     - 如果对方返回了cookie信息，可以通过返回结果查看返回的cookiejar实例
     - 可以将cookiejar转化成字典格式
     - cookiejar = rsp.cookies
     - cookiedict = reuqest.urils.dict_from_cookiejar(cookiejar)
     
- session
    - 和服务器端的session不同
    - 模拟一次会话，从客户端浏览器连接服务器开始，到客户端浏览器断开
    - 能然我们跨请求保持某些参数，比如在同一个session实例发出的所有请求之间保持cookie
    
            # 创建session对象，可以保存cookie值
            ss = request.session()
            
            headers = {"User-Agent":xxxx}
            data = {"name":xxxx}
            
            # 此时，发出的请求不用request,或者get之类，由创建的session管理请求,负责发出请求
            ss.post("http://www.baidu.com", data=data, headers=headers)
            
            rsp = ss.get("xxxx")
            
- https请求验证ssl证书
    - 参数verify负责表示是否需要验证ssl证书，默认时True
    - 如果不需要验证ssl证书，则设置成False表示关闭。
    
            rsp = request.get("https://www.baidu.com", verify=False)
        
        
        
        
        
        
        
        
        
        
        
        
        