from flask import Flask,render_template
app = Flask(__name__)

@app.route('/<name>')
def index(name):
    candidates = ['harsh','srishti','nilesh','kiran']
    return render_template('basic_mode_controlflow.html',candidates = candidates,name=name)

app.run(debug=True)