from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = '1poeijf8fh18vnjao'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()