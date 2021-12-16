from os import name
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>enter /letsupghrade/names</h2>'

@app.route('/letsupgrade/<names>')
def letsupgrade(names):
    return render_template('basic_mode_variable.html',name=names)
 
app.run(debug=True)