from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


def getListCurr():
    return ['USD', 'CHF', 'EUR']


class ListCurr(FlaskForm):
    btSelect = SubmitField("Выбрать")
    list = getListCurr()
    listCurr = SelectField("Валюта:", validate_choice=True,
                           choices=list)

    def validate(self, extra_validators=None):
        if self.listCurr.raw_data == self.listCurr.data:
            return False
        return True
