import urllib
'''
使用parse对url参数进行编码
get方式
'''
if __name__ == "__main__":
    url = "http://www.baidu.com/s?"
    rsp = urllib.request.urlopen(url)
    wd = input("请输入关键字")
    qs = {
        "wd": wd
    }
    # 转为url编码
    qs = urllib.parse.urlencode(qs)
    fullurl = url + qs
    print(fullurl)
    rsp = urllib.request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)