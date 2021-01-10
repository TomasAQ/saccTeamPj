import connOracle
import connMongo
import pandas as pd


# 실황 , 예보데이터에 일별 최고기온과 날짜를 리턴해준다.
def prtemp(smon , emon , focast ,col):
    # col  :  hitemp ,  lotemp , avgtemp
    liitems = []
    foitems = []
    smon = int(smon)
    emon = int(emon)
    focast =focast
    col = col
    for mon in range(smon , (emon+1)) :
        for day in range(1,32) :
            lilist = connOracle.selectTLIdayData("2020" + str(mon).zfill(2) + str(day).zfill(2), col)
            folist = connMongo.fotempmonlist(mon,day,focast,"temperature")
            if folist :
                liitems.append(lilist)
                if col =="hitemp" :
                    foitems.append(["2020"+str(mon).zfill(2)+str(day).zfill(2),max(folist)])
                elif col == "lotemp" :
                    foitems.append(["2020" + str(mon).zfill(2) + str(day).zfill(2), min(folist)])
                elif col == "avgtemp" :
                    foitems.append(["2020" + str(mon).zfill(2) + str(day).zfill(2), sum(folist) / len(folist)])

    return liitems , foitems


# 정확도를 계산해주는 함수
def accuracy(liitems , foitems):
    liitems = liitems
    foitems = foitems
    correctCnt = 0

    for i in range(len(foitems)) :

        if liitems[i][0][0] == foitems[i][0] :
            checkData = liitems[i][0][1]
            if foitems[i][1] >= checkData -2 and foitems[i][1] <= checkData +2 :
                correctCnt = correctCnt +1
    # 정확도 , 비교데이터 개수
    return round( (correctCnt / len(foitems) )  * 100) , len(foitems)

# list 두개를 dataframe 으로 변경해주는 함수
def makepdDataFrame(liitems , foitems):
    liitems = liitems
    foitems = foitems
    pdliday = []
    pdlival = []
    pdfoday = []
    pdfoval = []
    for i in range(len(liitems)):
        pdliday.append(liitems[i][0][0])
        pdlival.append(liitems[i][0][1])
        pdfoday.append(foitems[i][0])
        pdfoval.append(foitems[i][1])


    return pd.DataFrame(x for x in zip(pdliday, pdlival, pdfoday, pdfoval))


#if __name__ == '__main__':
    # col  :  hitemp ,  lotemp , avgtemp
    #liitems , foitems = prtemp(1,1,"6.0","hitemp")
    #a , b = accuracy(liitems , foitems)

