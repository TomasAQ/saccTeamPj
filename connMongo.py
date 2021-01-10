import pymongo
from pymongo import MongoClient
import pandas as pd
import data.connInfo as dbinfo

def mongoConn() :
    global conn , collect , foCYeondong;
    host, port = dbinfo.mongoInfo()

    conn = MongoClient(host, port)
    # weater 라는 이름의 데이터베이스가 만들어짐
    db = conn.weather
    # weater에 cheonYeondong 컬렉션 생성
    collect = db.cheonYeondong
    foCYeondong = db.focheonYeondong

# mongodb 접속
#def mongoConn() :


# csv 파일 읽고 안에 있는 데이터 넣기
# 초기에 한번만 실행
# 천연동 실황 데이터
def insertlicheonyeondongData() :
    dfChen_Y = pd.read_csv("cheon_yeondong.csv")

    for i in  range(len(dfChen_Y)):
        # 컬럼 명
        #a, day, hour, precipitation_form, humidity, precipitation, temperature, date = dfChen_Y.loc[[i]]
        # 테이터
        a, dayVal, hourVal, precipitation_formVal, humidityVal, precipitationVal, temperatureVal, dateVal = dfChen_Y.loc[i]

        collect.insert_one({'date': str(dateVal) , 'day' : str(dayVal) , 'hour' : str(hourVal) , 'precipitationForm' : float(precipitation_formVal) , 'humidity' : float(humidityVal) , 'precipitation' : float(precipitationVal) , 'temperature' : float(temperatureVal) })
# 천연동 관측 데이터
def insertfocheonyeondongData() :
    dffoCh = pd.read_csv("fo_cheon_yeondong.csv")
    for i in range(len(dffoCh)) :
        # 컬럼명
        # a, format: day,hour,forecast,precipitation_form,humidity,precipitation,temperature,date
        a, dayVal, hourVal, forecastVal ,precipitation_formVal, humidityVal, precipitationVal, temperatureVal, dateVal =dffoCh.loc[i]
        foCYeondong.insert_one({'date': str(dateVal), 'day': str(dayVal), 'hour': str(hourVal),'forecast':str(forecastVal),'precipitationForm': float(precipitation_formVal), 'humidity': float(humidityVal),'precipitation': float(precipitationVal), 'temperature': float(temperatureVal)})

    print('complet add data')


# collection 전체 제거
def delectAllCollect() :
    # 전체 문서 삭제
    collect.drop()
    # 항목 하나 삭제
    #collect.delete_one({'202001' : {'format: day' : 1} })


# collection 내용 변경
def updateEx() :
    #collect.update_one({'no': 1}, {'$set': {'kor': 100, 'eng': 100}})
    pass

# 천연동 실황데이터
def showlicheonyeondong() :
    rows = collect.find()
    for row in rows :
        print(row)

    #print(rows.count())
    # 8784

def showfocheonyeondong():
    rows = foCYeondong.find()
    for row in rows:
        print(row)

    #print(rows.count())
    # 43082


    #print(collect.count())

# 일별 기온을 list로 리턴
def tempmonlist(mon,day):
    mongoConn()
    tempday = '2020'+str(mon).zfill(2)+' '+str(day)

    #rows = collect.find({'date': '202001 1'}).sort("temperature", pymongo.ASCENDING)
    rows = collect.find({'date': tempday}).sort("temperature", pymongo.DESCENDING)

    #rows = collect.find({'date': '202001 1'})
    #rows = collect.find({'temperature':0.3})

    #rows = collect.find({'date': '202001 1'}).sort({'temperature':-1})
    #rows = collect.find({'date': '202001 1'})

    templist = []
    for row in rows:
        temp = row['temperature']
        templist.append(temp)

    return  templist


# 일별 강수량 데이터를 list에 담아서 리턴
def precipitationlist(mon,day):
    mongoConn()
    precday = '2020' + str(mon).zfill(2) + ' ' + str(day)

    # rows = collect.find({'date': '202001 1'}).sort("temperature", pymongo.ASCENDING)
    rows = collect.find({'date': precday}).sort("precipitation", pymongo.DESCENDING)

    preclist = []
    for row in rows :
        prec = row['precipitation']
        preclist.append(prec)

    return preclist

def hltemp() :
    mongoConn()
    htemp = collect.find({}).limit(1).sort("temperature", pymongo.DESCENDING)
    ltemp = collect.find({"temperature":{"$gt":-50}}).limit(1).sort("temperature", pymongo.ASCENDING)
    #ltemp = collect.find({}).limit(10).sort("temperature", pymongo.ASCENDING)


    for row in htemp :
        #print(row)
        hitempval = row['temperature']
        hitempdayval = row['date']

    for row in ltemp:
        #print(row)
        lotempval = row['temperature']
        lotempdayval = row['date']

    return hitempval,hitempdayval.replace(" ",""),lotempval,lotempdayval.replace(" ","")

# 접속 종료
#def dbOut() :
#    collect.close()
#    conn.close()

# 실황데이터 와 관측데이터에 최고 기온 비교
def comcheonhilotemp():
    mongoConn()
    li = collect.find({}).limit(3).sort("temperature", pymongo.DESCENDING)
    fo = foCYeondong.find({}).limit(3).sort("temperature",pymongo.DESCENDING)
    licheon = []
    focheon = []
    for row in li:
        #licheon.append(row['temperature'])
        licheon.append(row)

    for row in fo:
        focheon.append(row)

    print(licheon)
    print(focheon)
    
# 일별 예보데이터를 가져온다.
def comcheonday(mon, day,focast):
    tempday = '2020'+str(mon).zfill(2)+' '+str(day)
    focast = focast
    mongoConn()
    fo = foCYeondong.find({'date': tempday,'forecast':focast})
    list = []
    for row in fo :
       list.append(row)
    return list

# 일별 예보데이터 중 원하는 데이터를 갸져온다.
def fotempmonlist(mon,day,focast,col):
    tempday = '2020' + str(mon).zfill(2) + ' ' + str(day)
    focast = focast
    mongoConn()
    fo = foCYeondong.find({'date': tempday, 'forecast': focast})

    templist = []
    for row in fo:
        temp = row[col]
        templist.append(temp)

    return  templist

# # 일별 최고,최저 기온,평균기온 , 총강수량 가져오기
def fodaydata(focast) :
    items = []
    focast = focast
    for mon in range(1, 13):
        for day in range(1, 32):
             temlist = fotempmonlist(mon,day,focast,'temperature')
             preclist = fotempmonlist(mon, day, focast, 'precipitation')
             if temlist:
                 items.append( ('106', '2020' + str(mon).zfill(2) + str(day).zfill(2), str(focast) ,max(temlist), min(temlist) , round(sum(temlist) / len(temlist),2) , round(sum(preclist),2) ) )

    return items


