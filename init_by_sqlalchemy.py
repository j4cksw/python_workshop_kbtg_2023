from app import app
from models import db, Items, Types


with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()