from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from apps.auth.schemas import KakaoRequestSchema, FaceBookRequestSchema
from apps.auth.usecases import KakaoAuthUseCase, FaceBookUseCase

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
    try:
        validator = FaceBookRequestSchema().load(data=request.args)
    except ValidationError:
        raise Exception

    token = FaceBookUseCase().execute(**validator)

    return jsonify({'token': token})

