# 클라이언트에서 서버로 페이지 요청시 데이터를 보내고자 한다
# 이때, case 1번 http의 메소드 방식을 이용하여 전송해본다
# GET 방식에 대한 이해

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/loginProc')
def loginProc():
        # 요청주소의 형태: URL?키=값&키=값...
        # uid, upw 추출 => 클라이언트가 보낸 데이터
        # 전달된 데이터는 어디를 타고 들어오는가? => 요청객체 => request
        # get 방식으로 전달된 데이터 추출
        # 개별 요청별로 알아서 전달되니까,request 객체를 바로 사용하면 된다
        uid = request.args.get('uid')
        upw = request.args.get('upw')
        print( uid,upw ) 
        return 'loginProc page'

@app.route('/')
def home():
        return "hello Flask Home page"


if __name__ == '__main__':
    app.run(debug=True)

