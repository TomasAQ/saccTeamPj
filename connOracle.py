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
    cur.execute("select * from TLIsedaemun ")
    res = cur.fetchall()
    for row in res:
        print(row)

def oraSelect() :
    # sql = "SELECT * FROM TLIsedaemun WHERE dcode=:dcode  AND idx=:idx"
    # cur.execute(sql , dcode='106' , idx=1)
    sql = "SELECT * FROM TLIsedaemun WHERE dcode=:dcode"
    cur.execute(sql, dcode='106')

    res = cur.fetchall()
    for row in res :
        #print(str(row[0])+"/////"+row[1])
        print(row)


def insertOrData() :

    items = [
        ('106' ,'천연동', 30, datetime.date(2020,12, 1 ), -10, datetime.date(2020,1, 1 )),
        ('107' ,'xx동', 31, datetime.date(2020,1, 1 ), -10, datetime.date(2020,12, 1 ))
    ]
    for row in items:
        sql = "INSERT INTO TLIsedaemun  VALUES(Slisedidx.nextval , :1,:2,:3,:4,:5,:6 )"
        cur.execute(sql,row)
    con.commit()


# 접속 종료
def dbOut() :
    cur.close()
    con.close()

if __name__ == '__main__':
    oraConn()
    # insertOrData()
    # test()
    oraSelect()
    dbOut()



