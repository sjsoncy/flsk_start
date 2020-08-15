# md?
-마크다운 표기법이자 파일명
```python
a = 3
b = 4
print(a+b)
```

# 큰제목
## 중제목
### 소제목
---

# flask **설치하려면**
- 가상환경 `virtualenv venv`
- `pip install flask`

# 기본 구조
- 웹 서버 실행 파일 **app.py**
- html 모아두는 **templates** 폴더
- 정적파일 모아두는 static 폴더

# app.py 스타트 코드
```python
from flask import Flask

# 서버 앱 생성
app = Flask(__name__)

#url 세팅 - 라우터 설정
dapp.route('/')
def index():
    return "<h1>인덱스 페이지</h1>"

# 앱실행
if __name__ == "__main__":
    app.run(debug=True) #가동
```

# 템플릿 연결 기본 예시
```python
#url 세팅 - 라우터 설정
dapp.route('/')
def index():
    # return "<h1>인덱스 페이지</h1>"
    return render_template("index.html")
```