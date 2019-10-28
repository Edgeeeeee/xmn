from urllib import request

'''
有cookie访问
'''
if __name__ == "__main__":
    url = "http://www.renren.com/971789497/profile"
    headers = {
        "Cookie": "anonymid=jyyfxwk4-finy79; depovince=GW; _r01_=1; jebe_key=a47a6070-ecfa-4d66-b64d-8ace4ebf9e72%7Cdd3ff819d08df3c63c7ed7a6e5d826b6%7C1565012574463%7C1%7C1565012576669; jebe_key=a47a6070-ecfa-4d66-b64d-8ace4ebf9e72%7Cdd3ff819d08df3c63c7ed7a6e5d826b6%7C1565012574463%7C1%7C1565012576671; ick_login=5250fd9c-420d-451a-b9d7-5d6a414a0381; jebecookies=cacf1bb7-264e-41f3-8c36-4ee8abaa9647|||||; JSESSIONID=abcq7R9_1VoHP5wa5aMXw; _de=1466C94A6ACC62DEF7DC708369CBDF64; p=df8adf826056f88199e07c146229e9137; first_login_flag=1; ln_uact=18845163129; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=fdef168927744a58fe29e3cca5742b207; societyguester=fdef168927744a58fe29e3cca5742b207; id=971789497; xnsid=99fc5140; ver=7.0; loginfrom=null; wp_fold=0"
    }
    try:
        req = request.Request(url=url,headers=headers)
        rst = request.urlopen(req)
        html = rst.read().decode("utf-8")
        print(html)
        with open("v11_renren_cookie.html", "w", encoding="utf-8") as f:
            f.write(html)
    except Exception as e:
        print(e)