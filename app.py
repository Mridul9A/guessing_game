from flask import Flask, render_template, request, redirect, url_for, session
from random import randint

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def index():
    session['number'] = randint(1, 100)
    session['guesses'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    session['guesses'] += 1
    number = session['number']

    if guess < number:
        message = "Higher number please"
    elif guess > number:
        message = "Lower number please"
    else:
        return redirect(url_for('result'))

    return render_template('guess.html', message=message, guesses=session['guesses'])

@app.route('/result')
def result():
    return render_template('result.html', number=session['number'], guesses=session['guesses'])

if __name__ == '__main__':
    app.run(debug=True)

