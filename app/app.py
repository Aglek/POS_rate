from flask import Flask, render_template, request
from lib.FlaskForm import ListCurr
from lib.currency import get_currency_rate
from lib.db import proc_rate_hist, create_table
from datetime import date, datetime, timezone
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ListCurr(request.form)
    form.listCurr.default = form.listCurr.choices[0]
    if form.validate_on_submit():
        currency = form.listCurr.data
        rate = get_currency_rate(currency)
        dt = datetime.now(timezone.utc)
        hist = proc_rate_hist(currency, rate, dt)
        return render_template('rate.html', title=currency,
                               rate=rate,
                               today=date.today().strftime("%d.%m.%Y"),
                               form=form,
                               hist=hist)
    return render_template('index.html',
                           today_day=date.today().strftime("%d.%m.%Y"),
                           form=form)


if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5001)
