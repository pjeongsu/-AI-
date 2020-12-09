import pymysql as my

def db_selectLogin( uid, upw ):
    conn = None
    row  = None 

    try:
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
            cursor.execute(sql, ( uid, upw ))
            row =cursor.fetchone()
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
                SELECT * FROM stock2 ORDER BY NAME ASC LIMIT %s, %s;
                '''
            amt       = onePage_dataNum
            startPage = (curPageId - 1 )*amt
            cursor.execute(sql, ( startPage, amt ))
            # cursor.execute(sql, ( 80, 100 ))
            rows =cursor.fetchall()
            # 결과를 다 가져와라
        #--------------------------------------------
    except Exception as e:
        print("예외 발생",e)
    finally:
        if conn : 
            conn.close()

    return rows




if __name__ == '__main__':
    # print( db_selectStockList() )
    
    # # 2페이지
    # print( db_selectStockList(1) )
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