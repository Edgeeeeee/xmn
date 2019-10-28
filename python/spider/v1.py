from urllib import  request

'''
使用urllib.request请求网页的内容，并打印出来
'''

if __name__ == '__main__':
    url = "https://www.zhaopin.com/"
    # 打开一个url，并把相应的页面内容作为返回
    rsp = request.urlopen(url)
    # 读取返回的结果，类型为bytes
    html = rsp.read()
    # 解码 转换成字符串。
    html = html.decode()
    print(html)
