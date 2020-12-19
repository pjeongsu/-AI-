# # 클라이언트에서 서버로 데이터를 보내는 조합
from flask import Flask, url_for


app = Flask(__name__)

# get 방식
@app.route('/')
def home():pass

# 전체적으로는 GET 방식 + 동적 파라미터
@app.route('/users/<uid>')
def users(uid):pass

# 전체적으로는 POST 방식 + 동적 파라미터
@app.route('/users/<uid>', methods=['POST'])
def join(uid):pass

#GET or POST or PUT 방식(rest API) + 동적 파라미터
@app.route('/signup/<uid>', methods=['POST','GET','PUT'])
def signup(uid):pass

# URL 테스트
# 플라스크 내부에서 url 테스트 기능 지원
with app.test_request_context():
    #as 따로붙일필요없어서 안붙이는거
    print('홈페이지', url_for('home'))
    print('동적파라미터', url_for('users',uid='유저'))


if __name__ == '__main__':
    app.run(debug=True)

