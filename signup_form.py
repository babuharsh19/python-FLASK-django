from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/signup')
def signup():
    Username = request.args.get('username')
    lower_letter = False
    upper_letter = False
    num_end = True
    lower_letter = any(s.islower() for s in Username )
    upper_letter = any(s.isupper() for s in Username )
    num_end = not((Username[-1]).isdigit())
    report = lower_letter and upper_letter and num_end
    return render_template('signup_form.html',username=Username)

@app.route('/thank')
def thanks():
    return render_template('thankyou.html')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
    
@app.route('/error')
def error_handle():
    return render_template('error_handle.html')

app.run(debug = True)