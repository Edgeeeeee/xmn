from flask import Flask, redirect, after_this_request, jsonify, make_response, url_for, request, session, abort, g

from datetime import timedelta



app = Flask(__name__)
app.secret_key = 'hahaha'

@app.before_first_request
def first():
    print("刷新cookie和session保存时间")
    app.permanent_session_lifetime = timedelta(minutes=5)  # session失效时间，五分钟之后过期

# 所有请求之前
@app.before_request
def before():
    g.name = request.args.get("name")  # 全局访问，请求之前创建，请求结束后销毁
# 所有请求之后
# @app.after_request
# def after(aa):
#     print('after all request')
#     return aa


@app.route('/')
@app.route('/<name>', methods=['GET','POST'])  # 同时接收post和get请求。
def index(name='haha'):
    # print(app.config['ADMIN_NAME'])
    # print(url_for('index'))
    # print(type(request.args.get("name")))
    # print(request.scheme)
    # print(type(request.values.get("name")))
    # print(request.user_agent)
    # @after_this_request
    # def after_this(a):
    #     print('after index request')
    #     return a


    # return 'hahah', 302, {'location':'https://www.baidu.com'}
    return '<h1><a href=%S>hello </h1>'

@app.route('/set_cookie/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('index') or request.referrer))
    response.set_cookie("name",name,timedelta(minutes=5))  # 第三个参数是设置cookie的过期时间。
    response.set_cookie("human","human")

    session["log_in"] = True
    return response

@app.route('/get_cookie')
def get_cookie():
    name = request.args.get("name")
    if name == None:
        name = request.cookies.get("name","Human")
    print(type(name))
    print(name)
    return 'ok'

@app.route('/error403')
def error403():
    abort(403)

@app.route('/session_pop')
def session_pop():
    try:
        session.pop("log_in")
    except Exception as  e:
        print(e)
    print(Flask.permanent_session_lifetime)


    return '退出成功'

@app.route('/setbackurl')
def setbackurl():
    return "<a href=%s>hahah</a>" % url_for("back_url", next=request.full_path)

@app.route('/back_url')
def back_url():
    return redirect(request.args.get("next"),url_for("index"))



def login_and_redirect():
    '''
    未登录状态执行登陆状态操作时
    调用此函数登陆
    登陆后将跳转到上一个url
    上一个url为空时跳转到index
    '''
    for target in request.args.get("next"), request.referrer:
        if target:
            return redirect(target)
        return redirect(url_for("index"))

if __name__ == '__main__':
    # app.config['ADMIN_NAME'] = 'XuMengnan'
    app.run(debug=True)
