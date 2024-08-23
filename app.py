from flask import Flask, render_template, request
from lib.FlaskForm import ListCurr
from lib.currency import get_currency_rate
from datetime import date
# import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5f4fa7f2-5265-477c-8552-651b9683ef82'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ListCurr(request.form)
    # form.listCurr.choices = getListCurr()
    form.listCurr.default = form.listCurr.choices[0]
    if form.validate_on_submit():
        currency = form.listCurr.data
        rate = get_currency_rate(currency)
        return render_template('rate.html', title=currency,
                               rate=rate,
                               today_day=date.today().strftime("%d.%m.%Y"),
                               form=form)
    return render_template('index.html',
                           today_day=date.today().strftime("%d.%m.%Y"),
                           form=form)
