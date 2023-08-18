from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

items_types = db.Table('items_types',
                    db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
                    db.Column('type_id', db.Integer, db.ForeignKey('types.id'))
                    )

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    price = db.Column(db.Float)
    type = db.relationship('Types', secondary=items_types, backref='items')

    def __repr__(self):
        return f"id {self.id} title { self.title } price { self.price} types { self.type }"
    
class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)

    def __repr__(self):
        return f"id {self.id} title { self.title }"