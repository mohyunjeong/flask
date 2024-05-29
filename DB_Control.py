import cx_Oracle

# DB 연결 및 커서 생성 함수
def db_conn() :
    user_name = "hr"
    password = "12345"

    dsn = "127.0.0.1:1521/xe"

    try :
        conn = cx_Oracle.connect(user_name, password, dsn)
        cur = conn.cursor()
        print("DB 연결 성공")
        
        # 연결 객체, 커서 객체를 반환
        return conn, cur
    
    except cx_Oracle.DatabaseError as e :
        print("Error : ", e)

        
# 테이블 생성 함수
def create_tbl(conn, cur) :
    query = """create table flask_table (
        code varchar(10) primary key,
        name varchar(10) not null,
        age integer not null)"""
    
    try :
        # 쿼리문을 DB로 전송해서 실행
        # 커서를 통해서 실행 성공 유무를 반환 (실패하면 -1를 반환)
        cur.execute(query)
        
        # 실행결과를 DB에 반영
        conn.commit()
        print("테이블 생성 완료")
        
    except cx_Oracle.DatabaseError as e :
        print("Error : ", e)
        
        
# 테이블에 데이터를 저장하는 함수
def insert_tbl(conn, cur, code, name, age) :
    # 입력된 값들을 딕셔너리로 생성
    input_data = {"code" : code, "name" : name, "age" : age}
    
    # 딕셔너리의 키 값을 쿼리문에 설정해서 생성
    query = "insert into flask_table values (:code, :name, :age)"
    
    try :
        # 딕셔너리 값을 query문에 할당해서 DB로 전송하고 실행
        cur.execute(query, input_data)
        
        conn.commit()
        print("테이블 저장 완료")
        
    except cx_Oracle.DatabaseError as e :
        print("Error : ", e)
        
        
# 테이블의 데이터 전체를 검색하는 함수
def search_all_tbl(conn, cur) :
    query = "select * from flask_table"
    
    try :
        cur.execute(query)
        
        # 커서 객체에서 반환된 값을 받는다
        # fetchall() : 전체 데이터를 받는다
        # fetchone() : 하나의 데이터를 받는다
        row = cur.fetchall()
        
        return row
        
    except cx_Oracle.DatabaseError as e :
        print("Error : ", e)
        
        
# 테이블의 조건에 맞는 code를 기준으로 검색하는 함수
def search_tbl(conn, cur, code) :
    input_data = {"code" : code}
    
    query = "select * from flask_table where code = :code"
    
    try :
        cur.execute(query, input_data)
        row = cur.fetchall()
        
        return row
        
    except cx_Oracle.DatabaseError as e :
        print("Error : ", e)
        
        
# 업데이트 함수
def update_tbl(conn, cur, code, name, age) :
    query = f"update flask_table set name = '{name}', age = {age} where code = '{code}'"
    
    # input_data = {"code" :code, "name" :name, "age" : age}
    # query = "update flask_table set name = :name, age = :age where code = :code"
    
    try :
        cur.execute(query)
        # cur.execute(query, input_data)
        
        conn.commit()
        print("테이블 수정 완료")
        
    except cx_Oracle.DatabaseError as e :
        print("Error : ", e)
        

# 삭제 함수
def delete_tbl(conn, cur, code) :
    # 1) 파라미커로 받은 데이터를 딕셔너리로 만든다
    input_data = {"code" :code}
    
    # 2) query문을 정의 - '콜론:변수명' 형태로 딕셔너리의 키 값 위치를 설정
    query = "delete from flask_table where code = :code"
    
    # 3) 예외처리
    try :
        
        # 4) excute()로 쿼리를 전송해 실행, 딕셔너리 할당
        cur.execute(query, input_data)
        
        # 5) 실행 결과를 DB에 반영
        conn.commit()
        print("데이터 삭제 완료")
        
    except cx_Oracle.DatabaseError as e :
        print("Error : ", e)

        
# DB 연결 종료 함수
def db_disconn(conn, cur) :
    cur.close()
    conn.close()
