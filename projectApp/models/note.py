from utils.db import db


class Note(db.Model):
    id_note = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable = False)
    code = db.Column(db.Integer(), nullable=False)
    customer = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150))
    date = db.Column(db.Date(), nullable=False)
    status = db.Column(db.Enum("Pagado", "Sin pagar"))
    total = db.Column(db.DECIMAL(10, 2), nullable=False)

    def __init__(self, code, customer, description, date, status, total):
        self.code = code
        self.customer = customer
        self.description = description
        self.date = date
        self.status = status
        self.total = total
    