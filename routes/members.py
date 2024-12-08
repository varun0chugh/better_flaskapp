from flask import Blueprint, jsonify, request
from models import Member
from database import members_db, add_member, get_member, delete_member, list_members
from helper.pagination import paginate

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/', methods=['GET'])
def get_members():
    
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    members = list_members()
    result = paginate(members, page, per_page)
    return jsonify(result), 200

@members_blueprint.route('/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    member = get_member(member_id)
    if member:
        return jsonify(vars(member)), 200
    return jsonify({'message': 'Member not found'}), 404

@members_blueprint.route('/', methods=['POST'])
def add_new_member():
    data = request.json
    member = Member(
        member_id=len(members_db) + 1,
        name=data['name'],
        email=data['email']
    )
    add_member(member)
    return jsonify(vars(member)), 201

@members_blueprint.route('/<int:member_id>', methods=['DELETE'])
def delete_member_by_id(member_id):
    member = delete_member(member_id)
    if member:
        return jsonify({'message': 'Member deleted'}), 200
    return jsonify({'message': 'Member not found'}), 404

@members_blueprint.route('/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member = get_member(member_id)
    if not member:
        return jsonify({'message': 'Member not found'}), 404
    data = request.json
    member.name = data.get('name', member.name)
    member.email = data.get('email', member.email)
    return jsonify(vars(member)), 200
