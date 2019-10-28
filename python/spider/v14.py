from urllib import request,parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登陆
    需要输入用户名，密码，用来获取cookie凭证
    :return:
    '''

    # 此url从form的action中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登陆form的两个对应的input中提取name属性
    data = {
        "email": "18845163129",
        "password": "buzhidaoa."
    }
    # 对data编码
    data = parse.urlencode(data)

    # 创建一个请求对象。
    req = request.Request(url=url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/971789497/profile"

    # 如果已经执行了login函数，则opener已经包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("v13_auto_cookie_renren.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == '__main__':
    '''
    执行完login后，会得到授权之后的cookie
    尝试把cookie打印出来
    '''
    login()
    print(cookie)

    for i in cookie:
        print("="*100)
        print(type(i))
        print(i)
        for j in dir(i):
            print(j)
