import chardet
from urllib import request

if __name__ == '__main__':
    url = "http://news.baidu.com/"
    rsp = request.urlopen(url)
    html = rsp.read()
    print(type(rsp))
    print(rsp)
    print(rsp.geturl())
    print(rsp.getcode())
    print(rsp.info())

    # # 利用chardet自动检测
    # cs = chardet.detect(html)
    # print(type(cs))
    # print(cs)
    # print("*"*100)
    # html = html.decode(cs.get("encoding", "urf-8"))
    # print(html)