from flask import Flask
from routes.books import books_blueprint
from routes.members import members_blueprint
from routes.auth import auth_blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.register_blueprint(books_blueprint, url_prefix='/api/books')
app.register_blueprint(members_blueprint, url_prefix='/api/members')
app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(debug=True)
