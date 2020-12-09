import pymysql as my

def db_selectLogin( uid, upw ):
    conn = None
    row  = None 

    try:
        conn = my.connect(   host    ='localhost',                    
                            user    ='root',
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
            cursor.execute(sql, ( uid, upw ))
            row = cursor.fetchone()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row

def db_selectStockList( curPageId=1 , onePage_dataNum=5 ):
    conn = None
    rows  = None 

    try:
        conn= my.connect(   host    ='localhost',                    
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                SELECT * FROM stocks ORDER BY NAME ASC LIMIT %s, %s;
                '''
            # 한 페이지에서 보여지는 데이터의 총수
            amt       = onePage_dataNum
            # 데이터를 가져오는 시작위치
            startPage = (curPageId - 1 )*amt
            cursor.execute(sql, ( startPage, amt ))
            rows =cursor.fetchall()
            # 결과를 다 가져와라
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows

def db_selectNameStock( keyword ):
    conn = None
    rows  = None 

    try:
        conn= my.connect(   host    ='localhost',                    
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            # 파라미터를 무조건 execute()를 통해서 넣을 필요는 없다
            sql ='''
                SELECT * FROM stocks WHERE NAME like '%{}%';
            '''.format(keyword)
            cursor.execute(sql)
            rows =cursor.fetchall()
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows

# 종목코드를 넣어서 해당 종목 1개의 상세 정보를 가져온다
def db_selectStockByCode( code ):
    conn = None
    row  = None 

    try:
        conn= my.connect(   host    ='localhost',                    
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                    SELECT * FROM stocks WHERE CODE = %s; 
            '''
            cursor.execute(sql, code)
            row =cursor.fetchone()
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return row

# 코드와 일치하는 종목의 정보를 수정한다
# 성공하면 1, 실패하면 0
def db_updateStockInfo(code, indu, pro):
    conn = None
    result = 0
    try:
        conn= my.connect(   host    ='localhost',                    
                            user    ='root',
                            password='12341234',
                            port    = 3306,
                            db      ='python_db',
                            charset ='utf8mb4',
                            cursorclass=my.cursors.DictCursor
                        )
        # ---------------------------------
        with conn.cursor( ) as cursor:
            sql ='''
                UPDATE 
                    python_db.stocks
                SET
                    indu = %s,
                    pro = %s
                WHERE
                    code = %s;
            '''
            cursor.execute(sql, (indu, pro, code))
    
        # 디비에 실제 반영을 수행
        conn.commit() # 커밋 -> 실반영 -> 성공/실패 여부를 알 수 있다
        result = conn.affected_rows() # 영향을 받은 수 => 0 or 1 <=
        # ---------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return result


if __name__ == '__main__':
    print(db_updateStockInfo('309930', '금융 지원 서비스업1', '기업인수합병1'))
    if 0:
        # # 2페이지
        print( db_selectStockList(1) )
        # print( db_selectStockList(2) )
        # print( db_selectStockList(3) )
        # # 첫페이지 요청 , 7개를 가져와라
        # print( db_selectStockList(1,7) )

    if 0:
        row = db_selectLogin('ho','232')
        print(row)
        row = db_selectLogin('guest','1234')
        print(row)
        print('-'*30)
        row = db_selectLogin('guest','211232')
        print(row)