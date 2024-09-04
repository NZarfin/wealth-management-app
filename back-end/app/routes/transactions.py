from flask import Blueprint, request, jsonify
from ..models.transaction import Transaction, db , TransactionType
from ..models.client import Client

transactions_bp = Blueprint('transactions_bp', __name__)

@transactions_bp.route('/transactions', methods=['GET'])
def get_transactions():
    client_id = request.args.get('client_id')
    if client_id:
        transactions = Transaction.query.filter_by(client_id=client_id).all()
    else:
        transactions = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transactions]), 200

@transactions_bp.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        return jsonify(transaction.to_dict()), 200
    else:
        return jsonify({'error': 'Transaction not found'}), 404

@transactions_bp.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    client_id = data.get('client_id')
    date = data.get('date')
    amount = data.get('amount')
    transaction_type = data.get('type')

    if not Client.query.get(client_id):
        return jsonify({'error': 'Client not found'}), 404

    new_transaction = Transaction(
        client_id=client_id,
        date=date,
        amount=amount,
        type=TransactionType(transaction_type)
    )
    db.session.add(new_transaction)
    db.session.commit()

    return jsonify({'message': 'Transaction created successfully', 'transaction': new_transaction.to_dict()}), 201

@transactions_bp.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'error': 'Transaction not found'}), 404

    db.session.delete(transaction)
    db.session.commit()

    return jsonify({'message': 'Transaction deleted successfully'}), 200
