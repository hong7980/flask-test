from flask import Flask,url_for
app =Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def hello2(name):
          return'Welcome,%s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('hello2',name= 'hong'))
    print(url_for('hello2',name='hongshui'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return  'Test page'

