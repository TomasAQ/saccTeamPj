import cx_Oracle
import datetime
import data.connInfo as dbInfo
import pandas as pd
import connMongo as mongoData


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



# 서대문구 실황 테이블
def insertTLIsedaemun() :
    items = []
    hitemp, hitempday, lotemp, lotempday = mongoData.hltemp()

    items.append(('106', '천연동', hitemp,hitempday,lotemp,lotempday))
    for row in items:
        sql = "INSERT INTO TLIsedaemun  VALUES(Slisedidx.nextval , :1,:2,:3,:4,:5,:6 )"
        con.cursor().execute(sql,row)
    con.commit()

# 서대문구 일별 실황 테이블
def insertTLIsedaemunday() :
    items = []
    for mon in range(1,13) :
        for day in range(1,32) :
            temlist = mongoData.tempmonlist(mon, day)
            preclist = mongoData.precipitationlist(mon, day)
            if temlist :
                items.append(('106', '2020'+str(mon).zfill(2)+str(day).zfill(2), max(temlist) , min(temlist) ,  sum(temlist) / len(temlist) , sum(preclist)))

    # 데이터 insert query
    for row in items:
        sql = "INSERT INTO TLIsedaemunday  VALUES(Sliseddayidx.nextval , :1,:2,:3,:4,:5,:6)"
        cur.execute(sql, row)
    con.commit()

    print('inert data : '+str(len(items)));


def selectTLI(dcode) :
    oraConn()
    dcode = dcode
    # sql = "SELECT * FROM TLIsedaemun WHERE dcode=:dcode  AND idx=:idx"
    # cur.execute(sql , dcode='106' , idx=1)
    sql = "SELECT * FROM TLIsedaemun WHERE dcode=:dcode"
    cur.execute(sql, dcode=str(dcode))
    res = cur.fetchall()

    for row in res :
        #print(str(row[0])+"/////"+row[1])
        result = row
    dbOut()
    return result
# 일별로 저장된 실황 데이터 가져오기
def selectTLIday():
    oraConn()
    sql = "SELECT * FROM TLIsedaemunday ORDER BY lidate "
    cur.execute(sql)
    res = cur.fetchall()
    result = []
    for row in res :
        result.append(row)

    dbOut()
    return result

def selectTLIdayData(date , col):
    oraConn()
    date =date
    col = col
    if col == "hitemp" :
        sql = "select lidate , hitemp from TLIsedaemunday where lidate=:lidate ORDER BY lidate "
    elif col == "lotemp" :
        sql = "select lidate , lotemp from TLIsedaemunday where lidate=:lidate ORDER BY lidate "
    elif col == "avgtemp" :
        sql = "select lidate , avgtemp from TLIsedaemunday where lidate=:lidate ORDER BY lidate "
    elif col == "totpcp" :
        sql = "select lidate , totpcp from TLIsedaemunday where lidate=:lidate ORDER BY lidate "

    cur.execute(sql, lidate=date )
    res = cur.fetchall()

    dbOut()
    return res

# 접속 종료
def dbOut() :
    cur.close()
    con.close()

