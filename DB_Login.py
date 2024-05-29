import cx_Oracle

# DB 접속함수
# username : 아이디, password : 암호, dsn : 주소
def db_conn() :
    username = 'hr'
    password = '12345'
    dsn = '127.0.0.1:1521/xe'

    try:
        conn = cx_Oracle.connect(username, password, dsn)
        cur = conn.cursor()
        print("접속 완료")
        
        return cur, conn  
    
    except cx_Oracle.DatabaseError as e:
        print("error ", e)  

# DB 접속 종료 함수
# cur : 현제 커서 객체, conn : 현재 연결 객체
def db_disconn(cur, conn) :
    cur.close()
    conn.close()  
    print("접속 종료")

# DB의 해당 테이블에 데이터를 저장하는 함수
def insertData(cur, conn, t_name, id, pw, name) :
    input_data = {"id":id, "pw":pw, "name":name}

    # 딕셔너리의 키 값으로 query문을 만든다
    query = f"insert into member_table values (:id, :pw, :name)"
          
    try:
        cur.execute(query, input_data)
        conn.commit()
        print("입력 완료")
        
    except cx_Oracle.DatabaseError as e:
        print("error ", e)

# DB의 해당 테이블에서 하나의 데이터를 검색하는 함수
def searchData(cur, conn, id, pw) :
    input_data = {"id":id, "pw":pw}
    query = f"select name from member_table where id=:id and pw=:pw"

    try:
        cur.execute(query, input_data)
        row = cur.fetchall()

        return row
    
    except cx_Oracle.DatabaseError as e:
        print("error ", e)
