

from flask import Flask, render_template, request, redirect
from db.d_5 import db_selectLogin
app = Flask(__name__)

@app.route('/')
def home():
        return "hello Flask Home page"



# RestAPI 기법을 이용하여 한개의 URL에서 메소드를 기준으로 분기 처리
# URL을 남발하지 않고, 업무별로 한개의 URL에서 다 처리되게 구성
# methods = ['GET','POST',...]
@app.route('/login', methods = ['GET','POST'] )
def login():
        # 모든 요청은 request 타고 들어오는 거임
        if request.method =='GET': # 보통 화면 처리 담당
                return render_template('login3.html')
        else:
                uid = request.form.get('uid')
                upw = request.form.get('upw')
                user = db_selectLogin( uid, upw )

                if user:  
                    return redirect('/') 
                else:
                    return render_template('alert.html')



if __name__ == '__main__':
    app.run(debug=True)

