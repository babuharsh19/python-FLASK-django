from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'go to /letsupgrade/name'
def decapitalize(s):
    if not s:  # check that s is not empty string
        return s
    return s[0].lower() + s[1:]
@app.route('/letsupgrade/<name>')
def letsupgrade(name):
    return render_template('basic_mode_filter.html',name=name)

app.run(debug=True)