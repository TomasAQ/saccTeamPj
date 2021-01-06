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
        con.cursor().execute(sql,row)
    con.commit()




def insertTLIsedaemunday() :
    #1. csv 파일에서 일별 최고기온,최저기온,평균기온,총강수량
    #온도 , 강수량
    # temlist = mongoData.tempmonlist(1, 1)
    # preclist = mongoData.precipitationlist(1,1)

    items = []
    for mon in range(1,13) :
        for day in range(1,32) :
            temlist = mongoData.tempmonlist(mon, day)
            preclist = mongoData.precipitationlist(mon, day)
            if temlist :
                items.append(('106', '2020'+str(mon).zfill(2)+str(day).zfill(2), max(temlist) , min(temlist) ,  sum(temlist) / len(temlist) , sum(preclist)))

    # items = [
    #     ( '106', '202001', max(temlist) , min(temlist) ,  sum(temlist) / len(temlist) , sum(preclist) )
    # ]


    # 데이터 insert query
    for row in items:
        sql = "INSERT INTO TLIsedaemunday  VALUES(Sliseddayidx.nextval , :1,:2,:3,:4,:5,:6)"
        cur.execute(sql, row)
    con.commit()

    print('inert data : '+str(len(items)));


# 접속 종료
def dbOut() :
    cur.close()
    con.close()

def testmongodata() :
    for day in range(1,32) :
        list = mongoData.tempmonlist(1,day)

    print(list)

    print(max(list))
    print(min(list))
    print(sum(list)/len(list))


if __name__ == '__main__':
    #testmongodata()
    oraConn()
    insertTLIsedaemunday()
    #oraConn()
    # insertOrData()
    #test()
    #dbOut()
    
    #csv 파일처리
    #readCSVCY()


