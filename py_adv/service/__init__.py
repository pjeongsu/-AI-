from flask import Flask, request, url_for, redirect, jsonify, session, Blueprint

# 앱 생성, 기타 설정 구성
def create_app():
    app = Flask(__name__)
    # 기타 설정
    # 세션처리
    initSession( app )
    # 환경변수 로드
    initEnvironment( app )
    # 디비연결 처리(미리 특정 세션수만큼 연결해서, 풀에서 관리(빌려주고, 반납받고))
    from service.model import initDataBasePooling
    initDataBasePooling( app )
        # 매번 연결할때마다 소요되는 시간을 절약함, 최초 가동시만 느리고
        # 이런 기법을 풀링 : pooling
        # 예 ) 동접 200, 300, 1000등 미리 세션을 잡아서 동접 처리를 가능
    # 블루프린트 -> 기능별/ 카테고리별 라우트 처리를 분리
    initBlueprint( app )
    # 라이프사이클 처리 -> 요청~응답까지의 전 과정을 모니터링 가능한 함수들 존재
    initLifecycle( app )
        # 이런 함수를 통해서, 요청과 응답을 컨트롤하는 기법
    return app

def initSession(app):
    # 세션은 서버측에 클라이언트 정보를 저장하여 클라이언트의 접속 및 요청을 쉽게 컨트롤 하는 기술
    #     -> 서버 자원을 사용한다는 문제점  => 스토리지를 이용해서 세션처리하는 기술을 많이 사용
    # <-> 쿠키는 클라이언트측에 특정 정보를 저장하여 클라이언트의 인터렉션 통제/ 가이드 하는 기술
    #     -> 보안에 취약함
    # 세션 처리 1 : 세션 초기화(플라스크에서 지원하는)
    # 앱키를 지정한다
    # app.secret_key = '랜덤하게 해시값을 기록'
    app.secret_key = 'wodsaf21241dd4f5awo3j2o1'
    pass

def initEnvironment(app):
    # 시스템 환경 변수, 특정파일을 읽어서 환경변수로 로드, 클래스파일을 읽어서 로드
    # 1. 특정파일을 읽어서 환경변수로 로드
    app.config.from_pyfile('resource/config.cfg', silent= True)
    # 2. 클래스로부터 로드
    from service.config import FlaskConfig
    app.config.from_object(FlaskConfig)
    # 3. 환경변수 확인
    # print(app.config)
    for k, v in app.config.items():
        print(k,v)
    pass

def initBlueprint(app):
    @app.route('/')
    def home():
        # 쿠키값 추출
        cookie = request.cookies.get('uid')
        print(cookie)
        return '''
            <div>
                <h2>메인 페이지 : %s</h2>
                <a href = '/user/login'>로그아웃</a>
            </div>
        '''%cookie

    # 개별 페이지(라우팅된) 모듈을 먼저 포함
    # 모듈 가져오기는 => 그안에 있는 모든 코드를 메모리에 로드
    from service.controller import user        

    # 블루프린트 연결
    from service.controller import bp_user, bp_biz , bp_cms
    # # url_prefix를 통해서 실제적인 url 시작값이 결정된다
    app.register_blueprint( bp_user, url_prefix='/user' )
    app.register_blueprint( bp_biz , url_prefix='/biz' )
    app.register_blueprint( bp_cms , url_prefix='/cms' )
    
    pass
# 플라스크 상에서 진행되는 모든 요청과 응답은 라이프싸이클 관장하는 함수를 반드시 거친다
def initLifecycle(app):
    pass
    # 이미 존재하는 기능을 표현
    # 함수안에 함수 => 클로저

    
    @app.before_first_request
    def before_first_request():
        # 여기서 세션처리를 수행하여, 페이지가 많아도 간단하게 컨트롤 할 수 있다
        print( '서버가 가동하고 최초 요청시 1회 반응한다')

    @app.before_request
    def before_request():
        # 세션이 존재하는지 검사 => 'uid' in session
        # 세션값 추출 session['uid']
        # print(session, 'uid' in session, session['uid'])
        # print(session['uid'], uid in session)
        # print(request.url)
        if not 'uid' in session: # 세션이 없다
            # 로그인 페이지로 이동 -> 로그인 페이지 자체는 세션이 없다
            # 현재 진입한 페이지가 로그인 페이지가 아니면서, 세션이 없는 경우
            # http://127.0.0.1:5000/user/login
            # url_for('블루프린트별칭.해당URL에매칭된함수명') => '/user/login'
            if request.url.find(url_for('userBP.login')) < 0:
                # 로그인 페이지로 이동
                return redirect(url_for('userBP.login'))


        # 여기서 세션처리를 수행하여, 페이지가 많아도 간단하게 컨트롤 할 수 있다
        # 로그인 페이지만 세션 없이 통과
        # 나머지 모든 페이지는 세션 없으면 redirect -> 로그인
        print( '모든 요청은 여기를 거쳐간다')

    @app.after_request
    def after_request( res ):
        # 모든 응답, 혹은 특정 응답에 조작을 가하거나, 가감을 하고 싶다면 여기서 처리
        print('모든 응답이 지나가는 곳')
        return res

    @app.teardown_request
    def teardown_request( ex ):
        # 클라이언트가 잘 받아서 처리했다
        print('브라우저가 응답을 받고 렌더링해서 화면이 보인다면(실행)')
        return ''

    @app.teardown_appcontext 
    def teardown_appcontext( ex ):
        # 한개의 요청이 완벽하게 처리되었음을 인지
        print( 'http요청 컨텍스트가 종료되었다')
        pass

    pass