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

    # 결과
    #print(dfRes)
    #print(dfRes.columns)
    dfRes.to_csv("cheon_yeondong.csv")


if __name__ == '__main__':
    read_csv_df()
    get_csv_data()

