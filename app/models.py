from . import db

class Property(db.Model):

    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(255))
    no_room = db.Column(db.String(10))
    no_bath = db.Column(db.String(10))
    price = db.Column(db.String(20))
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