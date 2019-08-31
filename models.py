from app import db

class emojiResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bad = db.Column(db.Integer)
    neutral = db.Column(db.Integer)
    great = db.Column(db.Integer)
