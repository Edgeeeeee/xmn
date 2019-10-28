from urllib import request,error
'''
没有cookie访问
'''

url = "http://www.renren.com/971789497/profile"
try:
    rst = request.urlopen(url)
    html = rst.read().decode("utf-8")
    print(html)
    with open("v11_renren.html", "w" ,encoding="utf-8") as f:
        f.write(html)
except Exception as e:
    print(e)