from urllib import request,parse
from http import cookiejar

cookie = cookiejar.MozillaCookieJar()
cookie.load('v15_cookie.txt', ignore_expires=True, ignore_discard=True)

cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)

def getHomePage():
    url = "http://www.renren.com/971789497/profile"

    # 如果已经执行了login函数，则opener已经包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("v16_auto_cookie_load_renren.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()