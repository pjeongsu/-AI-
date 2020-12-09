import pymysql as my
# 1. 디비 연결
# 1-1. 디비 오픈
conn = None
try:
    conn= my.connect(   host    ='localhost', #'127.0.0.1'
                    user    ='root',
                    password='12341234',
                    port    = 3306,
                    db      ='python_db',
                    charset ='utf8mb4'
                )
    print('연결 성공')
except Exception as e:
    print("예외 발생",e)
finally:
    if conn : #변수가 False가 아닌 값을 가지고 있으면 참이다
        conn.close()
        print('해제 성공')