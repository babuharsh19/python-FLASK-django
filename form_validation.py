from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class Regform(Form):
    meal = StringField('Enter a meal from the above list ')
    submit = SubmitField('Submit')

@app.route('/register', methods=['Get', 'POST'])
def index():
    meals = {'dahi':'370 calories','paneer':'472 calories','pulses' : '252 calories','fruits' : '392 calories'}
    meal = False
    form = Regform(request.form)
    if form.validate():
        meal = form.meal.data
        form.meal.data=''
    return render_template('form_validation.html',meal=meal,form=form,diet=meals)
app.run(debug=True)