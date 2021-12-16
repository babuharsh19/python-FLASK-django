from flask import Flask,request
app = Flask(__name__)
@app.route("/")

def index():
    return "<h2>Welcome to the sever</h2>"

@app.route("/name/<your_name>/<work>")
def letsupgrade(your_name,work):
    if work[-1:-4]=='gni':
        sentence = your_name + " is " + work
    else:
        sentence = your_name + " is " + work+"ing"
    
    return sentence
app.run(debug=True)