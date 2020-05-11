'''
    创建应用程序，并注册相关蓝图
'''
import dataclasses
import uuid

from flask import Flask as _Flask

from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError
from datetime import date, datetime
from werkzeug.http import http_date

# from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager

# from app.libs.email import mail
# from flask_cache import Cache
# from app.libs.limiter import Limiter

__author__ = '带土'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, datetime):
            return http_date(o.utctimetuple())
        if isinstance(o, uuid.UUID):
            return str(o)
        if dataclasses and dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        raise ServerError()

class Flask(_Flask):
    json_encoder = JSONEncoder


login_manager = LoginManager()


# cache = Cache(config={'CACHE_TYPE': 'simple'})
# limiter = Limiter()


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

    from app.api.user import create_blueprint_user
    app.register_blueprint(create_blueprint_user(), url_prefix='/api/user')
    from app.api.cms import create_blueprint_cms
    app.register_blueprint(create_blueprint_cms(), url_prefix='/api/cms')
    from app.api.spider import create_blueprint_spider
    app.register_blueprint(create_blueprint_spider(), url_prefix='/api/spider')
    from app.api.shop import create_blueprint_shop
    app.register_blueprint(create_blueprint_shop(), url_prefix='/api/shop')


def register_plugin(app):
    from app.models.base import db
    # 注册SQLAlchemy
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app(config=None):
    app = Flask(__name__)

    #: load default configuration
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')

    # # 注册email模块
    # mail.init_app(app)
    #
    # # 注册login模块
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    #
    # # 注册flask-cache模块
    # cache.init_app(app)

    # 注册CSRF保护
    # csrf = CsrfProtect()
    # csrf.init_app(app)

    register_blueprint(app)
    register_plugin(app)

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app
