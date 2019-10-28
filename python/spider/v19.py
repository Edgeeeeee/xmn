'''
破解有道词典
js加密方法
处理js加密代码

1. 计算salt公式
salt: i = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
sigh: sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
2. 返回格式为压缩格式，需要解压缩，用gzip模块

'''

from urllib import request,parse
import time, random
from io import BytesIO
import gzip
import json


def getsalt():
    '''

    :return: salt
    '''
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt

def getmd5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign

def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    return getmd5(sign)


def youdao(key):
    salt = str(getsalt())
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt":salt,
        "sign": getSign(key,salt),
        "ts": salt[0:-1],
        "bv": "a4f4c82afd8bdba188e568d101be3f53",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME"
    }
    # print(data)

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

    # print(headers)
    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read()
    buff = BytesIO(html)
    f = gzip.GzipFile(fileobj=buff)
    res = f.read().decode('utf-8')
    res = json.loads(res)
    print(res["translateResult"][0][0]['tgt'])
    try:
        for i in res['smartResult']["entries"]:
            print(i,end="")
    except Exception as e:
        pass
if __name__ == '__main__':
    while 1:
        key = input('请输入要翻译的内容(英文 -> 中文)')
        youdao(key)
