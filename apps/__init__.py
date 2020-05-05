from flask import Flask

from apps.auth import kakao


def init_blueprint(app: Flask):
    app.register_blueprint(auth, url_prefix='/api/v1/auth/')


def create_app():
    app = Flask(__name__)
    init_blueprint(app=app)
    return app
