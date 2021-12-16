from flask import Flask, render_template, request, flash,session, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
class Regform(Form):
    candidate = StringField('Enter your name', validators=[DataRequired()])
    submit = SubmitField('Submit')
 
@app.route('/register', methods=['POST','GET'])
def register():
    form = Regform(request.form)
    if form.validate():
        candidate = form.candidate.data
        if (candidate.isdigit()):
            flash('enter correct name ')
        else:
            flash('welcome')
            

    return render_template('advance_validation_form.html',form=form )
if __name__ == "__main__":
    app.secret_key = 'super secret key'




    app.debug = True
    app.run()