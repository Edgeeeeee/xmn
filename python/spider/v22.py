'''
使用参数headers和params
研究返回结
'''
# 完整访问时下面的url加上参数构成
import requests
url = 'http://www.baidu.com/s?'
kw = {
    "wd":"王八蛋"
}

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
rsp = requests.get(url,kw,headers=headers)
print(rsp.text)
print(rsp.headers)
print(rsp.request)
print(rsp.content)
print(rsp.url)
print(rsp.status_code)

