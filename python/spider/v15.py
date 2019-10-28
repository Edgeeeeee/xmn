from urllib import request,parse
from http import cookiejar
'''
使用cookie登陆
自动获取cookie
'''
# 创建filecookiejar的实例
filename = "v15_cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
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

    # 保存cookie文件
    # ignore_discard 表示即使cookie将被丢弃也把它保存下来
    # ignore_expires表示如果该文件中cookie即使已经过期，也要保存下来
    cookie.save(ignore_discard=True, ignore_expires=True)




if __name__ == '__main__':
    login()
