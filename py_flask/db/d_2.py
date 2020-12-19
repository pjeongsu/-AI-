import pymysql as my
conn = None
try:
    conn= my.connect(   host    ='localhost',                    user    ='root',
                        password='12341234',
                        port    = 3306,
                        db      ='python_db',
                        charset ='utf8mb4'
                    )
    print('연결 성공')
    # ---------------------------------
    # SQL 실행, select 계열
    # cursor()를 통해 만들어지는 커서 객체로 쿼리수행
    with conn.cursor() as cursor:
        #1. sql문 준비
        sql ='''
            SELECT
                *
            FROM
                users
            WHERE
	            uid = 'guest' AND upw = '1234';
            '''
        #2. 쿼리 수행
        cursor.execute(sql)
        #3. 결과 집합 획득, 비동기적으로
        row =cursor.fetchone()
        #4. 후처리
        print( row )
        #4.1 이름을 출력하시오
        print( row[3])
        # 테이블 구조가 바뀌면 (컬럼순서변경) 이에따라
        # 개발자는 수정을 해야한다-> 구조가 변경되어도 서비스에 영향을 받지않게
        # 하고싶다 -> 순서애 기반해서 처리했다
        # => 순서에 상관없이 처리하는 구조로 업데이트 => dict로 교체
        print( row['name'])
        pass
    # -------------------------------
except Exception as e:
    print("예외 발생",e)
finally:
    if conn : 
        conn.close()
        print('해제 성공')