from databaseh import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    days = db.Column(db.Integer)
    price = db.Column(db.Integer)