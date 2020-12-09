# 풀링 기법을 적용하여
# 매 요청시 디비에 접속, 해제 하는 코드를 제외시켜서
# 서버 가동시 최초에 동접을 계산하여 커넥션을 미리 만들고
# 요청시 커넥션을 빌려주고, 사용 다 하면 반납받는 구조로 구성
# 클라이언트 입장에서 대기시간이 줄어든다 -> 빠른 응답처리가능
# 동시간 처리양이 증가 -> 서비스의 질이 향상

import pymysql as my
# pip(conda) install DBUtils
# 2.0 버전에서 명칭들이 일부 변경되었습니다.
from dbutils.pooled_db import PooledDB

class DBHelper:
    # 멤버변수는 생략해도 원하는 시점에 self.xxx = yy 라고 정의하면 바로 생성
    pool = None
    # 생성자
    def __init__(self, app):
        # 멤버변수 초기화
        # app은 Flask 객체인데 환경변수 정보를 가지고 있다
        # 디비 커넥션 풀 생성 -> 연결정보를 가지고 생성 -> 환경변수에서 가져온다
        self.pool =  PooledDB( creator = my
            ,host           = app.config['DB_TEST_URL']
            ,user           = app.config['DB_USER']
            ,password       = app.config['DB_PW']
            ,database       = app.config['DB_DATABASE']
            ,autocommit     = False
            ,charset        = app.config['DB_CHARSET']
            ,cursorclass    = my.cursors.DictCursor
            ,blocking       = False
            ,maxconnections = app.config['DB_MAX_POOL'] # 서버가동 즉시 디비와 100개의 커넥션을 맺는다
            )
        pass
    # 소멸자 -> 객체가 소멸하면 호출되는 요소 -> 서버가동중단 시점
    def __del__(self):
        # 디비연결해제(풀링에 연결된 모든 커넥션)
        if self.pool:
            self.pool.close()
        pass 
    # 멤버함수 -> 각종 쿼리 -> 나중에 별도로 빼서 처리
    # 로그인 처리(예시)
    def db_selectLogin( self, uid, upw ):
        conn = None
        row  = None 
        try:
            # 풀링에서 커넥션을 하나 빌려온다
            conn = self.pool.connection()
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
                cursor.execute(sql, ( uid, upw ))
                row =cursor.fetchone()
        except Exception as e:
            print("예외 발생",e)
        finally:
            if conn : 
                # 커넥션을 반납한다
                conn.close()
        return row

if __name__ == '__main__':
    dbHelper = DBHelper(None)
    print(dbHelper.db_selectLogin('jeong','0000'))