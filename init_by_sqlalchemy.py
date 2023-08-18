from app import app
from models import db, Items, Types


with app.app_context():
    #db.init_app(app)
    db.drop_all()
    db.create_all()

    types = [
        Types(title="book"),
        Types(title="food"),
        Types(title="stationary"),
        Types(title="liquor"),
    ]
    db.session.add_all(types)
    db.session.commit()