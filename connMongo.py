import pymongo
from pymongo import MongoClient
import pandas as pd
import data.connInfo as dbinfo


# mongodb 접속
def mongoConn() :
    global collect;
    host , port  = dbinfo.mongoInfo()

    conn =MongoClient(host, port)
    #weater 라는 이름의 데이터베이스가 만들어짐
    db=conn.weather
    #weater에 cheonYeondong 컬렉션 생성
    collect = db.cheonYeondong

# csv 파일 읽고 안에 있는 데이터 넣기
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

if __name__ == '__main__':
    mongoConn()
    # 초기에 한번만 실행
    #mongoInsertData()
    showData()

