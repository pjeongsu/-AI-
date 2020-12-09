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
    with conn.cursor( ) as cursor:
        # 쿼리문에 외부 데이터를 세팅하여 일반화 시킨다(파라미터 전달)
        # %s로 치환한다 <- '값' 을
        sql ='''
            SELECT
                *
            FROM
                users
            WHERE
	            uid = %s AND upw = %s;
            '''
        
        # 파라미터 전달하여 쿼리 수행
        cursor.execute(sql, ('ho','232'))
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