import pymongo
from pymongo import MongoClient
import pandas as pd
import data.connInfo as dbinfo

def mongoConn() :
    global collect , conn;
    host, port = dbinfo.mongoInfo()

    conn = MongoClient(host, port)
    # weater 라는 이름의 데이터베이스가 만들어짐
    db = conn.weather
    # weater에 cheonYeondong 컬렉션 생성
    collect = db.cheonYeondong

# mongodb 접속
#def mongoConn() :


# csv 파일 읽고 안에 있는 데이터 넣기
# 초기에 한번만 실행
def mongoInsertData() :
    dfChen_Y = pd.read_csv("cheon_yeondong.csv")

    for i in  range(len(dfChen_Y)):
        # 컬럼 명
        #a, day, hour, precipitation_form, humidity, precipitation, temperature, date = dfChen_Y.loc[[i]]
        # 테이터
        a, dayVal, hourVal, precipitation_formVal, humidityVal, precipitationVal, temperatureVal, dateVal = dfChen_Y.loc[i]

        collect.insert_one({'date': str(dateVal) , 'day' : str(dayVal) , 'hour' : str(hourVal) , 'precipitationForm' : float(precipitation_formVal) , 'humidity' : float(humidityVal) , 'precipitation' : float(precipitationVal) , 'temperature' : float(temperatureVal) })
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

# 모든 데이터 출려
def showData() :
    rows = collect.find()
    for row in rows :
        print(row)

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


# 접속 종료
#def dbOut() :
#    collect.close()
#    conn.close()



if __name__ == '__main__':
     # mongoConn()
     # showData()
     precipitationlist(1, 1)






