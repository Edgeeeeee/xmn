from urllib import request,error
'''
使用代理访问百度网站
'''
url = "http://www.baidu.com"
if __name__ == "__main__":
    # 使用代理步骤
    # 1. 设置代理地址
    proxy = {
        "http": '117.127.16.205:8080'
    }
    # 2. 创建ProxyHandler
    proxy_handeler = request.ProxyHandler(proxy)
    # 3. 创建opener
    opener = request.build_opener(proxy_handeler)
    # 4. 安装opener
    request.install_opener(opener)
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except Exception as e:
        print(e)