# 절차적코드는 누군가 import 해버리면 그 즉시 수행이 되버려서
# 의도하지 않고 코드가 작동해 버린다
# 원하는 시점에 작동하게 모듈화 하고 싶다면 -> 함수,클래스로 구성되어야한다 
import pymysql as my

def db_selectLogin( uid, upw ):
    conn = None
    row  = None # 함수의 리턴값

    try:
        # 차후 연결 정보를 일괄적으로 관리한다
        # 정보 변경시 다 고쳐야하는 문제, 요청이 올 때마다 매번 접속하면
        # TODO 느리다(응답이 느려질 수 밖에 없다)=> 개선이 필요
        conn= my.connect(   host    ='localhost',                    user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                SELECT
                    *
                FROM
                    users
                WHERE
                    uid = %s AND upw = %s;
                '''
                # %s에 대치되는 형태는 '변수값'
            cursor.execute(sql, ( uid, upw ))
            row =cursor.fetchone()
        # 문제가 없다면 여기서 회원정보가 세팅될 것
        # 만약 회원정보가 없다면 None으로 리턴
        # -------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()
    # 아이디, 비번이 일치 -> 데이터가 리턴
    # 연결오류, 혹은 아이디 비번 불일치 -> None

    return row

if __name__ == '__main__':
    # 단위 테스트를 하기위해서, 개별함수를 직접 테스트하기 위해서 삽입
    row = db_selectLogin('ho','232')
    print(row)
    row = db_selectLogin('guest','1234')
    print(row)
    print('-'*30)
    row = db_selectLogin('guest','211232')
    print(row)
    # 이코드는 나만 확인할 수 있고 다른사람이 당기면 작동안함