from flask import Flask
from models import db
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SECRET_KEY"] = "brigs070781"
bootstrap = Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db.init_app(app)

with app.app_context():
    db.create_all()

from routes import *

if __name__ == "__main__":
    app.run(debug=True)