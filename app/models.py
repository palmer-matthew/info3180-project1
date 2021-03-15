from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(255))
    no_room = db.Column(db.Integer)
    no_bath = db.Column(db.Integer)
    price = db.Column(db.Float)
    type = db.Column(db.String(20))
    location = db.Column(db.String(150))
    filename = db.Column(db.String(255)) 

    def __init__(self, title, description, no_room, no_bath, price, type, location, filename):
        self.title = title
        self.description = description
        self.no_room = no_room
        self.no_bath = no_bath
        self.price = price
        self.type = type
        self.location = location
        self.filename = filename