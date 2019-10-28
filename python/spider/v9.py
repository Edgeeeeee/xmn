'''
访问一个小网址，更高UserAgent进行伪装。
'''

from  urllib import request, error

if __name__ == "__main__":
    url = "http://www.baidu.com"
    try:
        headers = {}
        headers["UserAgent"] = "Mozilla/5.0 (iPad: CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
        # 另一种方式
        # req = request.Request(url)
        # req.add_header("User-Agent", "Mozilla/5.0 (iPad: CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")


        req = request.Request(url=url, headers=headers)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except Exception as e:
        print(e)