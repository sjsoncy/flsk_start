from flask import Flask, render_template

# 서버 앱 생성
app = Flask(__name__)

#url 세팅 - 라우터 설정
dapp.route('/')
def index():
    # return "<h1>인덱스 페이지</h1>"
    return render_template("index.html")

# 앱실행
if __name__ == "__main__":
    app.run(debug=True) #가동

