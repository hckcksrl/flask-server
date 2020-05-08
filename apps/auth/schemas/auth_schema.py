from marshmallow import Schema, fields, ValidationError, validates


class KakaoRequestSchema(Schema):
    code = fields.String(required=True)

    @validates('code')
    def validate_code(self, data):
        if len(data) == 0:
            raise ValidationError('validate error')


class FaceBookRequestSchema(Schema):
    code = fields.String(required=True)

    @validates('code')
    def validate_code(self, data):
        if len(data) == 0:
            raise ValidationError('validate error')
