# 파이썬을 이용하여 웹서비스를 개발하는 기술 습득
# 모델(머신러닝/ 딥러닝등으로 학습한 결과물)을 동일한 언어로 서비스하기 위해
# 파이썬으로 웹서비스 구성법을 익힌다( 단, 웹서비스시 )

# 플라스크를 이용한 웹사이트 기본구조 구현
# 실행 : python f_1.py

# 0단계 - 필요모듈설치
'''
    # $ pip install flask - 일반 파이썬 환경
    # $ conda install flask - 아나콘다 환경
'''

# step 1 : 모듈 가져오기
from flask import Flask



# step 2 : Flask 객체 생성
app = Flask(__name__)

# step 3 : 라우팅 : URL을 정의, 
# 특정 URL을 처리하는(요청을 처리, 응답을 구성, 실제 응답수행)
# 함수를 정의하여 매칭한다.
# 고유한 url 1개와 함수 1개를 매칭한다
# -> 전체       : 웹서비스, 기획서상의 스토리보드 존재가 필요
# -> 프로토클표 : 미들웨어 서비스, 화면이 없는 웹서비스, 통신만 수행함
#               이런 경우 웹이 화면, 서비스는 전부 클라이언트가 담당한다.
#               ex) reactjs, angular, vue => js or 타입스크립트로 클라이언트

# @ : 데코레이터
# '/' : URL -> 서버 상의 특정 페이지의 주소,
# '/' => 홈페이지를 의미함, http://naver.com

@app.route('/')
def home():
    # 함수 내부는 현재로써는 문자열을 리턴해야 한다! 이것만 유지
    return "hello Flask Home page"

# step 4 : 서버가동 -> 엔트리 포인트 지정, 시작점 설정
if __name__ == '__main__':
    # 서버 가동
    app.run(debug=True)



# 5000번은 flask의 시그니처 포트