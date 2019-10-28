'''
破解有道词典
'''

from urllib import request,parse
from datetime import datetime
from io import BytesIO
import gzip
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
def youdao(key):
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15681094158828",
        "sign": "e1e8c002f2d32ebe1c6610c8faebe872",
        "ts": "1568109415882",
        "bv": "a4f4c82afd8bdba188e568d101be3f53",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = parse.urlencode(data).encode()

    headers = {
        "Accept": r"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": r"gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Content-Length": "237",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=2139916500@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=422054782.21463114; JSESSIONID=aaaI-HM5kQy5G-WZe3z0w; ___rl__test__cookies=1568110311379",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"

    }


    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read()
    buff = BytesIO(html)
    f = gzip.GzipFile(fileobj=buff)
    res = f.read().decode('utf-8')

    print(res)
if __name__ == '__main__':
    youdao("girl")
