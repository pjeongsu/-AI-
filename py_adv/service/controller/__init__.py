# 블루프린트 클래스를 이용하여 기능별로 url을 부여
from flask import Blueprint

# 파라미터 : 별칭, 이름, static_folder(정적데이터폴더),
#           template_folder(html 위치)

# ~/user/~
bp_user = Blueprint('userBP', __name__
                    ,static_folder = '../static'
                    ,template_folder= '../template')

# ~/biz/~
bp_biz = Blueprint('bizBP', __name__
                    ,static_folder = '../static'
                    ,template_folder= '../template')

# ~/cms/~
bp_cms = Blueprint('cmsBP', __name__
                    ,static_folder = '../static'
                    ,template_folder= '../template')