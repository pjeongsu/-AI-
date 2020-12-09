import pymysql as my
conn = None
try:
    conn= my.connect(   host    ='localhost',                    user    ='root',
                        password='12341234',
                        port    = 3306,
                        db      ='python_db',
                        charset ='utf8mb4',
                        cursorclass=my.cursors.DictCursor
                    )
    print('연결 성공')
    # ---------------------------------
    # 결과 집합이 딕셔너리, [ 딕셔너리, 딕셔너리, ..] 이렇게 와야함
    #1. 연결할 때 dict로 받겟다.
    #2. 커서를 뽑을 때 dict로 처리하겠다(커서타입지정)
    # with conn.cursor( my.cursors.DictCursor) as cursor:
    with conn.cursor( ) as cursor:
        sql ='''
            SELECT
                *
            FROM
                users
            WHERE
	            uid = 'guest' AND upw = '1234';
            '''
        cursor.execute(sql)
        row =cursor.fetchone()
        print( row )
        print(row['name'])
        pass
    # -------------------------------
except Exception as e:
    print("예외 발생",e)
finally:
    if conn : 
        conn.close()
        print('해제 성공')