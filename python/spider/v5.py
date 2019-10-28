

'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
    打开F12
    尝试输入单词，每次输入都有请求
    利用network-all-headers 查看fromdata kw:gril
    检查返回内容格式，发现返回的是json格式，--》 需要用到json包
'''

import json
from urllib import request, parse

'''
流程是
    利用data构造内容，然后urlopen打开
    返回一个json格式的结果
    结果就应该是girl的释义
'''

baseurl = "https://fanyi.baidu.com/sug"
kw = input("输入关键字")
data = {
    "kw": kw
}
# 需要用parse模块对data编码
data = parse.urlencode(data).encode("utf-8")
print(type(data))

# 需要构造一个请求头，请求头部因该至少包含传入的数据的长度
# request要求传入的请求一定是一个dict格式
headers = {
    "Content-Length": len(data)
}

# 有了headers.data.url,就可以发出请求了
rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode()
print(json_data)

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)
for items in json_data['data']:
    print(items["k"] + "----" + items['v'])