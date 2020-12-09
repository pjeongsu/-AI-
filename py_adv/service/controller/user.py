# 본 페이지는 ~/user/ 이하의 서브 페이지들을 개발하는 공간
from flask import render_template, redirect, url_for, request, session, make_response
from service.controller import bp_user #as app
from service.model import dbHelper

# 기존의 라우트는
'''
    app은 Flask 객체이다
    @app.route('/')

    # 쿠키 처리, 파일업로드

    블루프린트에서는 블루프린트 객체를 이용하여서 라우트를 정의
    # ~/user/
    @bp_user.route('/')
'''
# ~/user
@bp_user.route('/')
def user_home():
    return '사용자 관련 홈페이지'

# ~/user/cookie

# http://127.0.0.1:5000/user/login
# ~/user/login, restFul 처리
@bp_user.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
            # 쿠키 처리를 위해서 응답 데이터를 조절할 수 있게 구성
            res = make_response(render_template('login.html'))
            # 쿠키 삽입 -> 어떤 이벤트에 의해서 수행 -> 여기서는 그냥 경제적으로 수행
            # 일반적으로는 쿠키는 유효시간을 지정해서 자동삭제하게 처리
            # 수동삭제 res.set_cookie('uid', '')
            # expires = 시간 => 파라미터를 부여하면 유효시간을 설정
            # path => 특정 쿠키가 적용되는 url을 지정
            res.set_cookie('uid', '게스트')
            return res
    else:
        # 1. 아이디 비번 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        # 2. 디비 쿼리
        user = dbHelper.db_selectLogin( uid, upw )
        if user:            
            # 3-1. 세션처리 -> 세션이 있는 사람만 홈페이지를 볼 수 있다.
            session['uid']= user['uid']
            # 3-2. 회원이면 홈으로
            # return redirect( url_for('') )
            return redirect('/')
        else:
            #  4. 안되면 팝업(alert)
            html = '''
            <script>
                alert("아이디 비번을 확인하세요");
                history.back();
            </script>
            '''
            return html
        # 로그인 처리


# ~/user/logout
@bp_user.route('/logout')
def logout():
    # 세션 제거
    if 'uid' in session:
        session.pop('uid', None)
    print(url_for('home'))
    return redirect(url_for('home'))
