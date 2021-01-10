from flask import Flask , render_template , request ,redirect , url_for
import connOracle
import connMongo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import predictionRate
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("hello.html")

@app.route('/analysis1')
def analysis1():
    return render_template("analysis1.html")

@app.route('/analysis2')
def analysis2():
    return render_template("analysis2.html")


@app.route('/analysis1result')
def analysis1result():
    startmon = request.args.get("startmon")
    endmon = request.args.get("endmon")
    forecast = request.args.get("forecast")
    #print(startmon , endmon , forecast)
    forecastVal = str(int(float(forecast)))

# 최고기온
    # 적중률
    liitems , foitems = predictionRate.prtemp(startmon,endmon,forecast,"hitemp")
    hitempPred , hitempitemscount =predictionRate.accuracy(liitems , foitems)

    #그래프

    # bar 그래프
    df = predictionRate.makepdDataFrame(liitems, foitems)
    df.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.barplot(data=df, x="day1", y="day1val")
    plt.savefig('./static/image/hitemp_bar1.jpg')
    plt.close()
    df = predictionRate.makepdDataFrame(liitems, foitems)
    df.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.barplot(data=df, x="day2", y="day2val")
    plt.savefig('./static/image/hitemp_bar2.jpg')
    plt.close()
    # line
    df2 = predictionRate.makepdDataFrame(liitems, foitems)
    df2.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.lineplot(data=df2, x="day1", y="day1val")
    sns.lineplot(data=df2, x="day2", y="day2val")
    plt.savefig('./static/image/hitemp_lin.jpg')
    plt.close()
    # scatter
    df3 = predictionRate.makepdDataFrame(liitems, foitems)
    df3.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.scatterplot(data=df3, x="day1", y="day1val")
    sns.scatterplot(data=df3, x="day2", y="day2val")
    plt.savefig('./static/image/hitemp_sca.jpg')
    plt.close()


# 최저기온
    # 적중률
    liitems, foitems = predictionRate.prtemp(startmon, endmon, forecast, "lotemp")
    lotempPred, lotempitemscount = predictionRate.accuracy(liitems, foitems)

    #그래프

    # bar 그래프
    df = predictionRate.makepdDataFrame(liitems, foitems)
    df.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.barplot(data=df, x="day1", y="day1val")
    plt.savefig('./static/image/lotemp_bar1.jpg')
    plt.close()
    df = predictionRate.makepdDataFrame(liitems, foitems)
    df.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.barplot(data=df, x="day2", y="day2val")
    plt.savefig('./static/image/lotemp_bar2.jpg')
    plt.close()
    # line
    df2 = predictionRate.makepdDataFrame(liitems, foitems)
    df2.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.lineplot(data=df2, x="day1", y="day1val")
    sns.lineplot(data=df2, x="day2", y="day2val")
    plt.savefig('./static/image/lotemp_lin.jpg')
    plt.close()
    # scatter
    df3 = predictionRate.makepdDataFrame(liitems, foitems)
    df3.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.scatterplot(data=df3, x="day1", y="day1val")
    sns.scatterplot(data=df3, x="day2", y="day2val")
    plt.savefig('./static/image/lotemp_sca.jpg')
    plt.close()

# 평균기온
    # 적중률
    liitems, foitems = predictionRate.prtemp(startmon, endmon, forecast, "avgtemp")
    avtempPred, avtempitemscount = predictionRate.accuracy(liitems, foitems)

    #그래프
    # bar 그래프
    df = predictionRate.makepdDataFrame(liitems, foitems)
    df.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.barplot(data=df, x="day1", y="day1val")
    plt.savefig('./static/image/avtemp_bar1.jpg')
    plt.close()
    df = predictionRate.makepdDataFrame(liitems, foitems)
    df.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.barplot(data=df, x="day2", y="day2val")
    plt.savefig('./static/image/avtemp_bar2.jpg')
    plt.close()
    # line
    df2 = predictionRate.makepdDataFrame(liitems, foitems)
    df2.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.lineplot(data=df2, x="day1", y="day1val")
    sns.lineplot(data=df2, x="day2", y="day2val")
    plt.savefig('./static/image/avtemp_lin.jpg')
    plt.close()
    # scatter
    df3 = predictionRate.makepdDataFrame(liitems, foitems)
    df3.columns = ['day1', 'day1val', 'day2', 'day2val']
    sns.scatterplot(data=df3, x="day1", y="day1val")
    sns.scatterplot(data=df3, x="day2", y="day2val")
    plt.savefig('./static/image/avtemp_sca.jpg')
    plt.close()


    return render_template("analysis1result.html" ,startmon=startmon , endmon = endmon , forecastVal = forecastVal , hitempPred = hitempPred , ihitempbar1="image/hitemp_bar1.jpg" ,ihitempbar2="image/hitemp_bar2.jpg" ,ihitemplin="image/hitemp_lin.jpg" , ihitempsca="image/hitemp_sca.jpg" ,lotempPred=lotempPred , ilotempbar1="image/lotemp_bar1.jpg" ,ilotempbar2="image/lotemp_bar2.jpg" ,ilotemplin="image/lotemp_lin.jpg" , ilotempsca="image/lotemp_sca.jpg" ,avtempPred=avtempPred , iavtempbar1="image/avtemp_bar1.jpg" ,iavtempbar2="image/avtemp_bar2.jpg" ,iavtemplin="image/avtemp_lin.jpg" , iavtempsca="image/avtemp_sca.jpg")


@app.route('/analysis1resultdetail')
def analysislresultdetail():
    forecast = request.args.get("forecastVal")
    print(forecast)
    forecast = str(float(int(forecast)))
    print(forecast)
    lilist = connOracle.selectTLIday()
    folist = connMongo.fodaydata(forecast)
    return render_template("daylist.html", li_list=lilist, fo_list=folist)


@app.route('/apply')
def apply():
    return render_template("apply.html")

@app.route('/analysis')
def analysis():
    mon = request.args.get("mon")
    location = request.args.get("location")
    temp = request.args.get("temp")
    prec = request.args.get("prec")

    list = connOracle.selectTLI(location)
    return render_template("list.html" , result_list = list)


@app.route('/list')
def list():
    list = connOracle.selectTLI('106')
    return render_template("list.html" , result_list = list)

@app.route('/daylist')
def daylist():
    lilist = connOracle.selectTLIday()
    folist = connMongo.fodaydata("1.0")
    #print(len(lilist) , len(folist))
    return render_template("daylist.html" , li_list = lilist , fo_list = folist)

@app.route('/grap')
def grap():
    list = connOracle.selectTLIday()
    #return render_template("grap.html" , result_list = list)
    df = pd.read_csv("cheon_yeondong.csv")

    sns.barplot(data=df, x="date", y="temperature")
    plt.savefig('./static/image/grap.jpg')

    #return render_template("grap.html" , photo =f"/static/image/grap.jpg")
    return render_template("grap.html" , image_file="image/grap.jpg")

def graptest() :
    liitems, foitems = predictionRate.prtemp(1, 1, "6.0", "hitemp")
    df = predictionRate.makepdDataFrame(liitems, foitems)
    df.columns =['day1','day1val','day2','day2val']
    sns.catplot(data=df, x="day1", y="day1val")
    sns.catplot(data=df, x="day2", y="day2val")
    plt.savefig('./static/image/hitemp_cat.jpg')

if __name__ == '__main__':
    app.run()
