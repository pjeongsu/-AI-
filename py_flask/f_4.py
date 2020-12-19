# URL 추가하기

from flask import Flask


app = Flask(__name__)


# URL 경로는 /구분자를 통해서 depth를 깊게 줄 수 있다.
@app.route('/')
def home():
        return "hello Flask Home page"

#~/users/login 유저의 로그인 홈페이지 
@app.route('/users/login')
def userlogin():
        return " user login home"

# ~/login
@app.route('/login')
def login():
        return "로그인 ID, 비밀번호"

@app.route('/logout')
def logout():
        return "logout"

if __name__ == '__main__':
    #1.
    app.run(debug=True)

    #2.
    # app.debug = True
    #80번포트는 http의 시그니처 포트라서 생략이 가능하다
    # run( 디버깅, 서버포트, 서버IP등등 사용자 설정이 가능하다)
    # app.run()

    # 두 방법 다 가능하다 -> 취향대로
