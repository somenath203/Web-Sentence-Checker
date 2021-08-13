from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def displayresult():

    upper_letter = False
    lower_letter = False
    digit_end = False

    username = request.args.get('username')

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    digit_end = username[-1].isdigit()

    result = lower_letter and upper_letter and digit_end

    return render_template('displayresult.html',username=username,result=result,lower=lower_letter,upper=upper_letter,digit_end=digit_end)


if __name__ == '__main__':
    app.run(debug=True)


 