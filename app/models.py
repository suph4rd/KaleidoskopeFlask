from app import db


class Footer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)


variables = locals()
