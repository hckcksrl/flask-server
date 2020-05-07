from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from apps.auth.schemas import KakaoRequestSchema
from apps.auth.usecases import KakaoAuthUseCase

auth = Blueprint('auth', __name__)


@auth.route('/kakao', methods=['GET'])
def kakao():
    try:
        validator = KakaoRequestSchema().load(data=request.args)
    except ValidationError:
        raise Exception

    token = KakaoAuthUseCase().execute(**validator)

    return jsonify({'token': token})


@auth.route('/facebook', methods=['GET'])
def facebook():
    return jsonify({'status': True})

