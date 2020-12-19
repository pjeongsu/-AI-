# 클라이언트가 특정 페이지를 요청할때, 데이터를 서버로 보낼 수 있다.
# case 1 : method를 이용하여 전송 = get, post, put, delete, ...
#          http 프로토콜을 이용하여 데이터 전송
#          메소드에 따라 목적과 방식, 스타일, 화면반응이 다르다
#          GET과 POST에 집중하여 작업
# case 2 : url에 실어서 전송 -> 동적파라미터(크기제한은 있음)
# <동적파라미터>

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
        return "hello Flask Home page"

#동적 파라미터 case 1 - 기본형
# 기자가 뉴스를 입력하면 고유 아이디를 부여하여 관리한다 
# 뉴스의 고유 아이디는 공개되도 상관없다
# http://127.0.0.1:5000/news/#%@~34123$!@$!
# 한글, 영대, 영소, 숫자, 특수문자 이상없음
# 한글을 코드에 붙이면 >> 인코딩 문자로 보임
# 한글이 그냥 가면 깨지기때문에 자동처리가 되었다(필요하면 수동처리)


# < 동적파라미터>
# 장점: 빠르게 서버쪽으로 데이터 전송하는 시스템구축 -> 프로토타입에 유리
@app.route('/news/<news_id>')
def news(news_id):
        # 함수 외부에서 함수 내부로 데이터를 전달하고 싶으면, 인자를 통해서 전달
        return "뉴스 %s" % news_id

@app.route('/news2/<pub_date>/<news_id>')
def news2(pub_date, news_id):
        return "뉴스 %s %s" % (pub_date, news_id)

# 보내는 데이터를 특정 타입으로 제한할 수 있는가?
# float, int, path(가변경로), 기본형은 문자열
# http://127.0.0.1:5000/news3/32131/2131241252141
# http://127.0.0.1:5000/news3/32131/2131241252141a -> not found
# -> 우리는 뉴스아이디를 인트로만 받기로했기 때문에
# 타입이 다르면 해당 페이지는 없다고 뜸

@app.route('/news3/<pub_date>/<int:news_id>')
def news3(pub_date, news_id):
        print(type(news_id))
        return "뉴스 %s %s" % (pub_date, news_id)


# 가변경로 
# http://127.0.0.1:5000/news4/a/b/c
# 데이터 => a/b/c => split 사용해서 데이터 가져올 수 있음
# url을 아무렇게나 쳐도 다 가변경로로 감
@app.route('/news4/<path:news_id>')
def news4(news_id):
        # /를 기준으로 분해하여 데이터를 각각 사용한다.
        print(news_id.split('/'))
        return "뉴스 %s " % news_id


if __name__ == '__main__':
    app.run(debug=True)

