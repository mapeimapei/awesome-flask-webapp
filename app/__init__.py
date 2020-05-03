'''
    创建应用程序，并注册相关蓝图
'''
from flask import Flask
from app.models import db

# from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager


#from flask_cache import Cache
# from app.libs.limiter import Limiter
# from app.libs.email import mail

__author__ = '带土'


login_manager = LoginManager()
#cache = Cache(config={'CACHE_TYPE': 'simple'})
#limiter = Limiter()


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def register_api_blueprint(app):
    from app.api import api
    app.register_blueprint(api, url_prefix='/api/cms')


def register_spider_blueprint(app):
    from app.spider import spider
    app.register_blueprint(spider, url_prefix='/api/spider')


def register_pet_shop_blueprint(app):
    from app.pet_shop import shop
    app.register_blueprint(shop, url_prefix='/api/shop')


def create_app(config=None):
    app = Flask(__name__)

    #: load default configuration
    app.config.from_object('app.settings')
    app.config.from_object('app.secure')

    # 注册SQLAlchemy
    db.init_app(app)

    # # 注册email模块
    # mail.init_app(app)
    #
    # # 注册login模块
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'


    # 注册flask-cache模块
    #cache.init_app(app)

    # 注册CSRF保护
    # csrf = CsrfProtect()
    # csrf.init_app(app)

    register_api_blueprint(app)
    register_web_blueprint(app)
    register_spider_blueprint(app)
    register_pet_shop_blueprint(app)

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app
