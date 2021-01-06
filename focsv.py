import pandas as pd

# 1. 판다스를 이용해서 csv 파일 읽어오기
def read_csv_df() :
    # 1.1. 전역으로 데이터를 어디서나 접근하기 위해서 전역으로 선언
    global dfPreF , dfHum, dfPre, dfTem , dfRes
    dfPreF = pd.read_csv("data/fo_cheon_yeondong_precipitation_form_202001_202012.csv")
    dfHum = pd.read_csv("data/fo_cheon_yeondong_humidity_202001_202012.csv")
    dfPre = pd.read_csv("data/fo_cheon_yeondong_precipitation_202001_202012.csv")
    dfTem = pd.read_csv("data/fo_cheon_yeondong_temperature_202001_202012.csv")


def get_csv_data() : 
    # 컬럼명 변경
    dfPreF.rename(columns={dfPreF.columns[3]: 'precipitation_form'}, inplace=True)
    dfHum.rename(columns={dfHum.columns[3]: 'humidity'}, inplace=True)
    dfPre.rename(columns={dfPre.columns[3]: 'precipitation'}, inplace=True)
    dfTem.rename(columns={dfTem.columns[3]: 'temperature'}, inplace=True)

    # 초기 컬럼 추가 4개
    dfRes = dfPreF
    # 컬럼 추가 1개
    dfRes['humidity'] = dfHum['humidity']
    dfRes['precipitation'] = dfPre['precipitation']
    dfRes['temperature'] = dfTem['temperature']

    # 결손값 제거
    dfRes = dfRes.dropna()

    #3721
    # date + 년월 추가해서 새로운 컬럼 생성
    dfRes['date'] = dfRes[' format: day']
    dfRes[:3720]['date'] = '202001'+dfRes[' format: day']
    dfRes[3720:7200]['date'] = '202002' + dfRes[' format: day']
    dfRes[7200:10920]['date'] = '202003' + dfRes[' format: day']
    dfRes[10920:14520]['date'] = '202004' + dfRes[' format: day']
    dfRes[14520:18241]['date'] = '202005' + dfRes[' format: day']
    dfRes[18241:21840]['date'] = '202006' + dfRes[' format: day']
    dfRes[21840:25560]['date'] = '202007' + dfRes[' format: day']
    dfRes[25560:28451]['date'] = '202008' + dfRes[' format: day']
    # 데이터 확인 필요 25일 까지 존재
    dfRes[28451:32045]['date'] = '202009' + dfRes[' format: day']
    dfRes[32045:35765]['date'] = '202010' + dfRes[' format: day']
    dfRes[35765:39364]['date'] = '202011' + dfRes[' format: day']
    dfRes[39364:]['date'] = '202012' + dfRes[' format: day']

    # csv 파일 만들기
    makeCsv(dfRes)

# csv파일 만들기
def makeCsv(dfRes) :
    dfRes = dfRes
    #dfRes.to_csv("fo_cheon_yeondong_nan.csv")
    dfRes.to_csv("fo_cheon_yeondong.csv")

if __name__ == '__main__':
    read_csv_df()
    read_csv_df()
    get_csv_data()