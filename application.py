from flask import Flask , render_template , request ,redirect , url_for
import connOracle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("hello.html")

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
    list = connOracle.selectTLIday()
    return render_template("daylist.html" , result_list = list)

@app.route('/grap')
def grap():
    list = connOracle.selectTLIday()
    #return render_template("grap.html" , result_list = list)

    df = pd.read_csv("cheon_yeondong.csv")
    sns.barplot(data=df, x="date", y="temperature")
    plt.savefig('./static/image/grap.jpg')

    #return render_template("grap.html" , photo =f"/static/image/grap.jpg")
    return render_template("grap.html" , image_file="image/grap.jpg")

if __name__ == '__main__':
    app.run()