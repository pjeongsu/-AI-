# html로 응답하기 -> 랜더링
# render_template이 렌더링을 수행하는데 기반이 되는 템플릿 엔진 : JinJa2
# JinJa2 기호 -> {..} <-> 타엔진 <%..%>
from flask import Flask,render_template


app = Flask(__name__)

@app.route('/show')
def show():
        # HTML을 수정한다고 해서 서버가 재가동되지는 않는다
        # html은 반드시 templates 폴더 이하에 파일로 저장해서 관리한다.
        return render_template('index.html')


@app.route('/')
def home():
        # 여기서 html을 보내주는 것은 맞으나, 그 긴 코드들을 문자열로 굳이 만들어서
        # 보내는것은 적합하지 않다 ->구조적, 유지보수적, 확장성 적으로 다 부적절함
        # -> render_template() 함수를 이용하여 처리
        # 엔트리 포인트에 templates 라는 폴더를 만들고 (현재는 이름 고정)
        # 그 밑에 html 파일을 두고, 참조하여 처리한다
        return '''<h1>html 직접 표현 </h1>'''


if __name__ == '__main__':
    app.run(debug=True)

