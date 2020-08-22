from flask import Flask, render_template, request

# 서버 앱 생성
app = Flask(__name__)

#url 세팅 - 라우터 설정
# @데코레이터 : 함수를 감싼다. 실행전 감싼고드부터 실행되게끔 한다.
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/framework')
def framework():
    return render_template("framework.html")

@app.route('/form')
def form():
    res = request.args.get('keyword') # args : arguments 입력인자. 매개변수를 입력할 떄 사용하는 말
    print(res)
    return render_template("form.html")

# 앱실행
if __name__ == "__main__":
    app.run(debug=True) #가동

