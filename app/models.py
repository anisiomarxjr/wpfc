from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    what = db.Column(db.String(100))
    where = db.Column(db.String(100))
    when = db.Column(db.DateTime)
    involveds = db.Column(db.String(100))
    reference = db.Column(db.String(100))
    how_much = db.Column(db.Float)
    classification = db.Column(db.String(3))

    def __repr__(self):
        return '<Entry %r>' % (self.text)
