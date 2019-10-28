

'''
利用request实现v5的内容。
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

# 设置一个Request实例
req = request.Request(url=baseurl, headers=headers, data=data)

# 因为已经构造了一个请求实例，则所有的请求信息可以封装在请求实例中。
rsp = request.urlopen(req)
json_data = rsp.read().decode()
print(json_data)

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)
for items in json_data['data']:
    print(items["k"] + "----" + items['v'])