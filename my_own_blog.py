from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
