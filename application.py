from flask import Flask , render_template , request ,redirect , url_for
import connOracle
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



if __name__ == '__main__':
    app.run()