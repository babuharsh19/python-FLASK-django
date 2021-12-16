from flask import Flask,render_template
app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('basic_mode.html')

app.run(debug=True)