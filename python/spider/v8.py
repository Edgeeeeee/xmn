from urllib import request, error

if __name__ == "__main__":
    url = "https://www.baidu.com"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e.reason)
    except error.HTTPError as e:
        print(e.reason)
    except Exception as e:
        print(e)
