from utils.db import db
from sqlalchemy.types import Enum as SqlEnum
import enum

class TransactionType(enum.Enum):
    credit = 'credit'
    debit = 'debit'

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    type = db.Column(SqlEnum(TransactionType), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'date': self.date.isoformat(),
            'amount': float(self.amount),
            'type': self.type.value
        }
