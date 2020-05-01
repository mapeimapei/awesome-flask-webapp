from flask import Blueprint, url_for

__author__ = '七月'

web = Blueprint('web', __name__, template_folder='templates')
#from app.web import test
from app.web import blog_list_handlers
from app.web import user_handlers
