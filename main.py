from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from birthday_paradox import birthday_paradox

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            ydays = int(request.form['Days'])
            pcnt = int(request.form['PersonCount'])
            drange = int(request.form['DaysRange'])
        except KeyError:
            return "Invalid request", 400
        res = birthday_paradox(ydays, drange, pcnt)
        if res[0]:
            return render_template('birthday_paradox.html', res=res[1], pcnt=pcnt, drange=drange)
        else:
            return render_template('birthday_paradox.html')
        

        return 'METHOD POST'
    else:
        return render_template('index.html')