from flask import Flask,render_template
app = Flask(__name__)

@app.route('/lets')
def letsupgrade():
    return render_template('navigation.html')

app.run(debug=True)