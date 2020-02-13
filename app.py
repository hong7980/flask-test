from flask import Flask, redirect, url_for,render_template

#import config.py

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', context={})


if __name__ == '__main__':
    app.run(debug=True)
