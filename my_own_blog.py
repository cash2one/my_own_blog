from flask import Flask
from flask_bootstrap import Bootstrap
from blog.index_view import index_page
from blog.log_view import log_page
from blog.test_view import test_page
from blog.detail_view import detail_page

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.register_blueprint(index_page)
app.register_blueprint(log_page)
app.register_blueprint(test_page)
app.register_blueprint(detail_page)

if __name__ == '__main__':
    app.run(debug=True)
