# -*- coding: utf-8 -*-
# 기본 템플릿
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
#from db.d_6 import db_selectLogin, db_selectStockList, db_selectNameStock
from db.d_6 import *
# [1] 웹소켓 통신용 모듈 가져오기
from flask_socketio import SocketIO

import os

app = Flask(__name__)
# 세션처리
app.secret_key = 'sakccsdcocjk2sdjkdskcj'
# [2] 시크릿키 지정 (환경변수)
app.config['SECRET_KEY'] = '12341234' #  비밀번호
# [3] SocketIO 생성시 Flask 객체를 래핑
socketio = SocketIO( app, cors_allowed_origins="*", async_mode='threading' )

@app.route('/')
def home():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('index.html', name='사용자명')

@app.route('/login', methods=['GET','POST'] )
def login():    
    if request.method == 'GET': # 화면 처리 담당
        return render_template('login.html') # View
    else: # POST
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        user = db_selectLogin( uid, upw )
        if user:
            return redirect( url_for('home') )
        else:        
            return render_template('alert.html')        

# 게시판 페이지
'''
    - M : Model => 파이썬으로 디비를 쿼리해서 결과를 C에게 돌려준다, 모듈제작
    - V : View  => html을 읽어서 JinJa2 엔진으로 랜더링하는 파트 개발->디자인영역
    - C : Controller => M,V를 조합해서 비즈니스로직을 구현하는 메인 파트
          요청을 분석해서 필요한 쿼리를 M에게 요청하고 그 결과를 받아서 V에서 랜더링을 지시
    - BluePrint를 적용하면 업무를 나눠서 각각 작업이 가능하다
'''
# ~/bbs?pageNo=1&amt=6
# get방식, 데이터는 pageNo, amt가 전달된다
@app.route('/bbs')
def bbs():
    # 주식 목록을 가져와서 뿌리겠다
    # None이면 1(첫번째페이지), 값이 존재하면 그값 그대로 세팅
    # 파라미터로 전달되는 데이터는 모둔 문자열이다
    # 따라서, int()로 형변환하여 페이지 계산할수 있게 전달한다
    # 1. step1 전달된 데이터 추출
    curPage = 1 if not request.args.get('pageNo') else int(request.args.get('pageNo'))
    amt     = 5 if not request.args.get('amt') else int(request.args.get('amt'))
    # 2. step2 데이터를 기반으로 비즈니스 로직 수행
    # 조회 결과를 가져온다(디비 쿼리 수행)
    rows    = db_selectStockList( curPage, amt )
    # 3. stpe3 랜더링후 결과를 응답해라
    return render_template('bbs.html', name='사용자명', stocks=rows)

@app.route('/search')
def search():   
    # 1. 검색어 추출
    keyword = request.args.get('k')
    # 2. 디비에 검색 쿼리 수행
    rows    = db_selectNameStock( keyword )
    # jsonify() : 파이썬 객체를 json 형태로 변환한다 
    # json은 리스트, 딕셔너리가 주된형태를 취한다
    # tmp = {
    #     "A":keyword
    # }
    # 응답 데이터에 화면(html)이 없다. 데이터만 있다 -> 미들웨어 서버
    return jsonify(rows) # jsonify(tmp)

@app.route('/detail', methods=['GET','POST'])
def detail():
    if request.method == 'GET':
        return render_template( 'detail.html', 
                                name='사용자명',
                                # 정보보기화면, 수정진행화면 분기 플래그 변수
                                # 1:정보보기화면, 2:수정하는화면
                                r=request.args.get('r'), 
                                stock=db_selectStockByCode( code=request.args.get('code') )
        )
    else:
        # 수정할 데이터 획득
        code    = request.form.get('code') 
        indu    = request.form.get('indu') 
        product = request.form.get('product')
        # 수정 쿼리 수행
        if db_updateStockInfo( code, indu, product ):# 성공
            # 수정이 성공하면 -> 팝업으로 알림 -> 
            # 알림 확인되면 => 다시 상세보기로 이동(수정된 내용이 보여야 한다)
            return render_template('msg.html', msg='수정 성공', 
                        url=url_for('detail')+'?r=1&code='+code )
        else:# 실패
            # 수정 실패하면 -> 팝업으로 알림, 되돌아가기        
            return render_template('msg.html', msg='수정 실패' )

@app.route('/chat')
def chat(): 
    return render_template('chat.html', name='사용자명')

@app.route('/upload', methods=['GET','POST'])
def upload(): 
    if request.method == 'GET':
        return render_template('upload.html', name='사용자명')
    else:
        # 파일 업로드 처리하는 부분
        f = request.files['file']        
        #print( os.path.abspath(__file__) )
        #print( os.path.dirname(os.path.abspath(__file__)) )
        #print( os.getcwd() )
        
        # 경로를 os에 상관없이 자동으로 계산해 준다
        dir = os.path.dirname(os.path.abspath(__file__))

        #print( dir + '/static/upload/' + f.filename  )
        # 파일 저장
        f.save( dir + '/static/upload/' + f.filename )
        return '''
            <h2>파일 업로드 완료</h2>
            <img src='/static/upload/%s'/>
        ''' % f.filename

###############################
# connect, disconnect 이런 이벤트명은 사전에 준비된 이벤트

# 클라이언트가 접속하면 자동호출
@socketio.on('connect')
def connect():
    print( '접속하였다' )

# 클라이언트가 접속 해제 자동호출
# 창을 닫아버리면 신호를 보낼 기회가 없어서, 해제이벤트를 받을수가 없다
# 단, 장시간 활동이 없으면 접속해제를 시행!!
@socketio.on('disconnect')
def disconnect():
    print( '접속해제' )

# 사용자가 정의한 이벤트 처리 등록
# 클라이언트가 보내는 이벤트중, 닉네임 보내는 이벤트 처리 핸들러
@socketio.on('c_send_userName')
def c_send_userName_handler( data, methods=['GET', 'POST'] ):
    print( '수신받은 데이터',  data )
    # 클라이언트가 서버에 접속하였다. 클라이언트 정보를 서버가 가지고 있어야 한다
    session['user'] = data['name']
    # 'xx'님이 입장하였습니다. => 메시지를 방(서버측에서 운영하는 방은 1개이다)에 방송
    # 서버가 클라이언트한테 이벤트를 발생, 데이터는 위의 메시지와 보낸사람 정보 
    socketio.emit('s_send_msg', { 'user':'방관리자', 'msg':f"{data['name']}님이 입장하였습니다." })

# 클라이언트가 보내는 이벤트중에, 메시지를 보내는 이벤트 처리 핸들러
@socketio.on('c_send_msg')
def c_send_msg_handler( data, methods=['GET', 'POST'] ):
    print( '수신받은 데이터',  data )
    socketio.emit('s_send_msg', data )

@socketio.on('customEvt')
def  customEvt_handler( data, methods=['GET', 'POST'] ):
    print( '수신받은 이벤트를 통해 전달된 데이터', data)

################################
if __name__ == '__main__':
    #app.run(debug=True)
    # [4] 소켓io를 이용하여 서버가동 (래핑해서 가동)
    socketio.run( app,  debug=True)