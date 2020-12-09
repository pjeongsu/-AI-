from service.model.dbHelper import DBHelper

# 클래스는 단 1회만 생성되어야 하고,
# 코드상의 어느곳이라도 다 사용할 수 있어야한다. -> 싱글톤 디자인 패턴

dbHelper = None

def initDataBasePooling(app):
    global dbHelper
    dbHelper = DBHelper(app)
    pass