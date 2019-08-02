from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

class Attributes(Form):
    plain = TextField('Enter plain GSM:', validators=[validators.DataRequired()])
    flute = TextField('Enter flute GSM:', validators=[validators.DataRequired()])
    length = TextField('Enter length in inches:', validators=[validators.DataRequired()])
    width = TextField('Enter width in inches:', validators=[validators.DataRequired()])
    sheet_count = TextField('Enter sheet count:', validators=[validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def hello():
    form = Attributes(request.form)
    print(form.errors)

    if request.method == 'POST':
        plain = float(request.form['plain'])
        flute = float(request.form['flute'])
        length = float(request.form['length'])
        width = float(request.form['width'])
        sheet_count = float(request.form['sheet_count'])

        sheet_area = (length*width*25.4*25.4)/(1000*1000)
        total_GSM = plain+(1.5*flute)
        sheet_weight = total_GSM * sheet_area
        production_weight = sheet_weight * sheet_count

        if production_weight>1000:
            production_weight1 = production_weight/1000
            return render_template('index.html', form=form, flute_weight=flute, plain_weight=plain, sheet_area=sheet_area, total_GSM=total_GSM, sheet_count=sheet_count, sheet_weight=sheet_weight, production_weight=str(production_weight1)+" kg")
        else:
            return render_template('index.html', form=form, flute_weight=flute, plain_weight=plain, sheet_area=sheet_area, total_GSM=total_GSM, sheet_count=sheet_count, sheet_weight=sheet_weight, production_weight=str(production_weight)+" grams")
   
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
