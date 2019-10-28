import chardet
from urllib import request
'''
利用requests下载页面。
自动检测页面编码
'''

if __name__ == '__main__':
    url = "http://news.baidu.com/"
    rsp = request.urlopen(url)
    html = rsp.read()

    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    print("*"*100)
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)