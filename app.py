import pymongo as pymongo
from flask import Flask,url_for,render_template

app =Flask(__name__)
client = pymongo.MongoClient(" mongodb + srv：// hongqijun：bdinbiot@cluster-flasktest - 8ucyh.azure.mongodb.net / test ？retryWrites = true&w = majority ")
#创建数据库flask—_test
db = client.flask_test
#创建集合
movie_collection=db.movie




#@app.route('/')
#def hello():
 #   return 'Hello'

@app.route('/user/<name>')
def hello2(name):
          return'Welcome,%s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'));
    print(url_for('hello2',name= 'hong'))
    print(url_for('hello2',name='hongshui'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return  'Test page'

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

name ='hong'
movies = [{'title':'book1','year':'1988'},
        {'title':'book2','year':'1488'},
        {'title':'book3','year':'1978'},
{'title':'book3','year':'1978'},
]

result = movie_collection.insert(movies)
print(result)