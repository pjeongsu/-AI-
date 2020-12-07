# 간단한 기본 서버 구축
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'aws 홈페이지'

# run.py가 엔트리포인트일 경우에만 작동
# 리눅스 서버로 가면 wsgi.py이 엔트리포이트이므로, 작동안함
# 패브릭을 설정한 룰에 의해서 서버가 작동된다
if __name__ == '__main__':
    app.run(debug=True)