from flask import Blueprint,jsonify
from flask import request
auth = Blueprint('auth', __name__)


@auth.route('/kakao', methods=['GET'])
def kakao() -> dict:
    return jsonify({'status': True})

