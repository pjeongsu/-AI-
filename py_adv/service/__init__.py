from flask import Flask, request, url_for, redirect, jsonify, session

# 앱 생성, 기타 설정 구성
def create_app():
    app = Flask(__name__)
    # 기타 설정 -----------------
    # 세션처리
    initSession(app)
    # 환경변수 로드
    initEnvironment(app)
    # 디비연결 처리(미리 특정 세션 수만큼 연결해서 풀에서 관리(빌려주고, 반납받고))
    from service.model import initDataBasePooling
    initDataBasePooling(app)
        # 매번 연결할 때마다 소요되는 시간을 절약, 최초 가동시만 느리고
        # 이런 기법을 풀링 : pooling
        # 예) 동접 200, 300, 1000 등 미리 세션을 잡아서 동접 처리를 가능
    # 블루프린트 -> 기능별/카테고리별 라우트 처리를 분리
    initBlueprint(app)
    # 라이프사이클 처리 -> 요청~응답까지의 전 과정을 모니터링 가능한 함수들 존재
    initLifecycle(app)
        # 이런 함수를 통해서, 요청과 응답을 컨트롤하는 기법
    return app

def initSession(app):
    # 세션은 서버측에 클라이언트 정보를 저장하여 클라이언트의 접속 및 요청을 쉽게 컨트롤 하는 기술
    #       -> 서버 자원을 사용한다는 문제점 => 스토리지를 이용하여 세션처리하는 기술을 많이 사용
    # <-> 쿠키는 클라이언트측에 특정 정보를 저장하여 클라이언트의 인터렉션 통제/가이드하는 기술
    #       -> 보안에 취약함
    # 세션 처리 1 : 세션 초기화(플라스크에서 지원하는)
    # 앱키를 지정한다
    app.secret_key = '랜덤하게 해시값을 기록'
    pass

def initEnvironment(app):
    pass

def initDataBasePooling(app):
    pass

def initBlueprint(app):

    @app.route('/')
    def home():
        return '홈페이지'
    pass

# 플라스크 상에서 진행되는 모든 요청과 응답은 라이프사이클 관장하는 함수를 반드시 가진다
def initLifecycle(app):
    
    # 이미 존재하는 기능을 표현
    # 함수 안에 함수 => 클로저
    @app.before_first_request
    def before_first_request():
        print('서버가 가동하고 최초 요청시 1회 반응한다')

    @app.before_request
    def before_request():
        # 여기서 세션처리를 수행하여, 페이지가 많아도 간단하게 컨트롤할 수 있다
        # 로그인 페이지만 세션 없이 통과
        # 나머지 모든 페이지는 세션 없으면 redirect -> 로그인
        print('모든 요청은 여기를 거쳐간다')
        pass

    @app.after_request
    def after_request(res):
        # 모든 응답, 혹은 특정 응답에 조작을 가하거나, 가감을 하고 싶다면 여기서 처리
        print('모든 응답이 지나가는 곳')
        return res

    @app.teardown_request
    def teardown_request(ex):
        # 클라이언트가 잘 받아서 처리했다
        print('브라우저가 응답을 받고 렌더링해서 화면이 보인다면(실행)')
        return ''

    @app.teardown_appcontext
    def teardown_appcontext(ex):
        # 한 개의 요청이 완벽하게 처리되었음을 인지
        print('http 요청 컨텍스트가 종료되었다')
        pass

    pass