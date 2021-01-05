import pandas as pd

# 1. 판다스를 이용해서 csv 파일 읽어오기
def read_csv_df() :
    # 1.1. 전역으로 데이터를 어디서나 접근하기 위해서 전역으로 선언
    global dfPreF , dfHum, dfPre, dfTem , dfRes
    dfPreF = pd.read_csv("data/cheon_yeondong_precipitation_form_202001_202012.csv")
    dfHum = pd.read_csv("data/cheon_yeondong_humidity_202001_202012.csv")
    dfPre = pd.read_csv("data/cheon_yeondong_precipitation_202001_202012.csv")
    dfTem = pd.read_csv("data/cheon_yeondong_temperature_202001_202012.csv")


#2. 필요한 데이터만 가져오기
def get_csv_data():
    # 컬럼명 변경
    dfPreF.rename(columns={dfPreF.columns[2] : 'precipitation_form'} , inplace=True)
    dfHum.rename(columns={dfHum.columns[2] : 'humidity'} , inplace=True)
    dfPre.rename(columns={dfPre.columns[2] : 'precipitation'} , inplace=True)
    dfTem.rename(columns={dfTem.columns[2] : 'temperature'} , inplace=True)

    # 초기 컬럼 추가 3개
    dfRes = dfPreF
    # 컬럼 추가 1개
    dfRes['humidity'] = dfHum['humidity']
    dfRes['precipitation'] = dfPre['precipitation']
    dfRes['temperature'] = dfTem['temperature']


    # 결손값 제거
    dfRes = dfRes.dropna()

    # 새로운 로직 필요
    # date + 년월 추가해서 새로운 컬럼 생성
    dfRes['date'] = dfRes[' format: day']
    dfRes[:744]['date'] = '202001' + dfRes[' format: day']
    dfRes[744:1440]['date'] = '202002' + dfRes[' format: day']
    dfRes[1440:2184]['date'] = '202003' + dfRes[' format: day']
    dfRes[2184:2904]['date'] = '202004' + dfRes[' format: day']
    dfRes[2904:3648]['date'] = '202005' + dfRes[' format: day']
    dfRes[3648:4368]['date'] = '202006' + dfRes[' format: day']
    dfRes[4368:5112]['date'] = '202007' + dfRes[' format: day']
    dfRes[5112:5856]['date'] = '202008' + dfRes[' format: day']
    dfRes[5856:6576]['date'] = '202009' + dfRes[' format: day']
    dfRes[6576:7320]['date'] = '202010' + dfRes[' format: day']
    dfRes[7320:8040]['date'] = '202011' + dfRes[' format: day']
    dfRes[8040:]['date'] = '202012' + dfRes[' format: day']


    #  조건 2개를 통한 값 불려오기
    # for01 = dfRes[' format: day'] == ' 1'
    # for02 = dfRes[' format: day'] == ' 2'
    # print(dfRes[for01 | for02].head(30))

    #csv 파일 만들기
    makeCsv(dfRes)
# csv파일 만들기
def makeCsv(dfRes) :
    dfRes = dfRes
    # dfRes.to_csv("cheon_yeondong_nan.csv")
    dfRes.to_csv("cheon_yeondong.csv")


if __name__ == '__main__':
    read_csv_df()
    get_csv_data()

