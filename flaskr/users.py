import functools

from flask import (
    Blueprint, jsonify, request
)

from flaskr.models import (db, User)
from flask import current_app
from flaskr.my_exception import My_Exception

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['Get'])
def get_users():
	users = User.query.all()
	return jsonify([u.serialize() for u in users])

@bp.route('', methods=['Post'])
def create_users():
	body = request.json
	current_app.logger.debug(body)
	user = User(email=body.get('email'), name=body.get('name'))
	db.session.add(user)
	db.session.commit()
	return jsonify(user.serialize())

@bp.route('/<int:user_id>', methods=['Get'])
def get_user_by_id(user_id):
	user = User.query.get(user_id)
	if user is None:
		raise My_Exception("User with id {} doesn't exist".format())
	return jsonify(user.serialize())

@bp.route('/<int:user_id>', methods=['Put'])
def update_user_by_id(user_id):
	user = User.query.get(user_id)
	if user is None:
		raise My_Exception("User with id {} doesn't exist".format())
	else:
		user.name = request.json.get('name')
		user.email = request.json.get('email')
	db.session.commit()
	return jsonify(user.serialize())