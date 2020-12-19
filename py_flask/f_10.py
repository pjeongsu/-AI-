

from flask import Flask, render_template, request, redirect, url_for
from db.d_5 import db_selectLogin
app = Flask(__name__)

@app.route('/')
def home():
        return "hello Flask Home page"



@app.route('/login', methods = ['GET','POST'] )
def login():
        if request.method =='GET': 
                return render_template('login3.html')
        else:
                uid = request.form.get('uid')
                upw = request.form.get('upw')
                user = db_selectLogin( uid, upw )

                if user:  
                    # 홈페이지 이동
                    # 필수요소 -> 가고싶은 곳의 주소를 써야함
                    # flask에서는 url을 직접 일력하는 것을 지양한다
                    # url이 바뀌면 사용하는 곳을 다 바꿔야해서
                    # url을 직접 기입하지 않아도 알아서 해당 url로 바꿔주는 기능
                    # => url_for('URL과 매칭된 함수명')을 쓰면된다
                #     return redirect('/')
                        return redirect (url_for("home"))
                else:
                    # Html에 데이터를 보내서 버무랴서 랜더링 할수 있는가?
                    # 답 : ok => flask가 사용하는 템플릿 엔진은 JinJa
                    # JinJa는 python 프로그래밍 언어를 위한 웹 템플릿 엔진이다
                    msg1 = ' [1] 회원이 아닙니다. 아이디, 비밀번호를 확인해주세요'
                    return render_template('alert2.html', msg=msg1)
                    # msg1 은 위의 msg1이라는 값을 의미 msg는 키 를 의미
                                                                                

if __name__ == '__main__':
    app.run(debug=True)

