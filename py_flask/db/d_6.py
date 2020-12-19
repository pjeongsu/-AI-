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

# 게시판에 한개의 페이지를 구성하는 데이터들을 조회하여 리턴한다
# 복수개의 데이터를 획득해서 리턴
# onePage_dataNum=5 : 기본적으로 5개를
# 한 페이지에서 보는 데이터량으로 구분, 정수값을 넣으라는 표시
# curPageId=1 : 기본 페이지는 1페이지이다
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
                SELECT NAME FROM stock ORDER BY NAME ASC LIMIT %s, %s;
                '''
            # 한 페이지에서 보여지는 데이터의 총수
            amt       = onePage_dataNum
            # 데이터를 가져오는 시작위치
            srartPage = (curPageId - 1 )*amt
            cursor.execute(sql, ( srartPage, amt ))
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
    
    # 2페이지
    print( db_selectStockList(1) )
    print( db_selectStockList(2) )
    print( db_selectStockList(3) )
    # 첫페이지 요청 , 7개를 가져와라
    print( db_selectStockList(1,7) )


    if 0:
        row = db_selectLogin('ho','232')
        print(row)
        row = db_selectLogin('guest','1234')
        print(row)
        print('-'*30)
        row = db_selectLogin('guest','211232')
        print(row)