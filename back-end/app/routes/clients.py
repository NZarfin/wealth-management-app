from flask import Blueprint, request, jsonify
from models.client import Client, db
from models.user import User

clients_bp = Blueprint('clients_bp', __name__)

@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.to_dict() for client in clients]), 200

@clients_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get(client_id)
    if client:
        return jsonify(client.to_dict()), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@clients_bp.route('/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    user_id = data.get('user_id')

    if not User.query.get(user_id):
        return jsonify({'error': 'User not found'}), 404

    new_client = Client(name=name, email=email, user_id=user_id)
    db.session.add(new_client)
    db.session.commit()

    return jsonify({'message': 'Client created successfully', 'client': new_client.to_dict()}), 201

@clients_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    data = request.get_json()
    client.name = data.get('name', client.name)
    client.email = data.get('email', client.email)

    db.session.commit()

    return jsonify({'message': 'Client updated successfully', 'client': client.to_dict()}), 200

@clients_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    db.session.delete(client)
    db.session.commit()

    return jsonify({'message': 'Client deleted successfully'}), 200
