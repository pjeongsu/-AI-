# 클래스에서 환경변수를 기록하고, 이를 사용한다
class FlaskConfig(object):
    # 멤버변수
    DB_TEST_URL = 'localhost'
    DB_REAL_URL = 'localhost' # 나중에 AWS로 연결
    DB_USER     = 'root'
    DB_PW       = '12341234'
    DB_DATABASE = 'python_db'
    DB_CHARSET  = 'utf8'
    DB_MAX_POOL = 100  # 풀링에서 최초에 연결하는 커넥션 수