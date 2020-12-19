

from flask import Flask, render_template, request, redirect
# 로그인 처리를 위한 회원정보조회 함수
from db.d_5 import db_selectLogin
app = Flask(__name__)

@app.route('/')
def home():
        # 세션 체크를 해서, 로그인 하지 않고 진입하면 팅겨서 로그인으로 던진다
        return "hello Flask Home page"


@app.route('/login') #Controller
def login():
        return render_template('login2.html') # View

# 기본은 GET만 허용한 라우팅
# @app.route('/loginProc')

#POST 만 허용한 라우팅
@app.route('/loginProc', methods = ['POST'])
def loginProc():
        # POST 방식: http의 바디를 타고 전송(가변크기)
        # 보안이 필요한 데이터, 파일(크기가 큰 데이터) 전송에 적합함
        # post 방식으로 데이터가 전달될 시 데이터 추출 방법      
        uid = request.form.get('uid')
        # uid = request.form['uid'] -> 이걸로 하면 잠재적으로 셧다운 발생소지가 있음 -> 키가없으면 셧다운된다
        upw = request.form.get('upw')
        # 데이터 베이스로 가서 이런 계정정보가 회원 목록에 있는지 조회한다
        user = db_selectLogin( uid, upw )
        # 파이썬에서 데이터베이스를 엑세스 하고, 쿼리를 수행하는 코드
        print(user)
        if user:  #회원이다
                # 세션 생성 ( 차후 추가 )
                # 메인 페이지로 이동 - 요청을 그대로 들고 다른 페이지로 던져라
                # => 리다이렉트
                return redirect('/') # 홈페이지 이동
        else:     #회원이 아니다.
                # 회원이 아님을 알린다(로그인실패) -> 팝업(JS로처리)
                return render_template('alert.html')
                # 다시 돌아와서 로그인 페이지 로드
                # alert.html 내부에 돌아오는거까지 있음
                # pass

        # print( uid,upw ) 
        # return 'loginProc page'


if __name__ == '__main__':
    app.run(debug=True)

