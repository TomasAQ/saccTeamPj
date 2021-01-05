import cx_Oracle
import datetime
import data.connInfo as dbInfo


def oraConn() :
    global con , cur
    dsn , id , pw = dbInfo.oracleInfo()
    dsn = dsn
    con = cx_Oracle.connect(id,pw, dsn)
    cur = con.cursor()

def test() :
    cur.execute("select * from pyoraTest ")
    res = cur.fetchall()
    for row in res:
        print(row)

def oraSelect() :
    #sql = "SELECT EMPNO , ENAME FROM EMP WHERE ENAME=:ENAME AND ENPNO:=enpno"
    sql = "SELECT EMPNO , ENAME FROM EMP WHERE ENAME=:ENAME AND EMPNO=:EMPNO"
    cur.execute(sql , ENAME='BLAKE' , EMPNO=7698)

    res = cur.fetchall()
    for row in res :
        #print(str(row[0])+"/////"+row[1])
        print(row)


def insertOrData() :
    items = [
        (8888, 'pythonin', 'CLERK', 7902, datetime.datetime(1980, 12, 17, 0, 0), 1300.0, None, 20),
        (8899, 'pythonin', 'CLERK', 7902, datetime.datetime(1980, 12, 17, 0, 0), 1300.0, None, 20)
    ]
    for row in items:
        sql = "insert into emp values(:1,:2,:3,:4,:5,:6,:7,:8)"
        cur.execute(sql,row)

    con.commit()


def insertOrData2() :
    items = [
        (8888, 'pythonin', 'CLERK', 7902, datetime.datetime(1980, 12, 17, 0, 0), 1300.0, None, 20),
        (8899, 'pythonin', 'CLERK', 7902, datetime.datetime(1980, 12, 17, 0, 0), 1300.0, None, 20)
    ]

    sql = "insert into emp values(:1,:2,:3,:4,:5,:6,:7,:8)"
    cur.bindarraysize = len(items)
    cur.execute(sql,items)

    con.commit()

# 접속 종료
def dbOut() :
    cur.close()
    con.close()

if __name__ == '__main__':
    oraConn()
    #oraSelect()
    test()
    #insertOrData()

    dbOut()



