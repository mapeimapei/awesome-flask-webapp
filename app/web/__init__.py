from flask import Blueprint, url_for

__author__ = '带土'

web = Blueprint('web', __name__, template_folder='templates')

#from app.web import test
from app.web import blog_handlers
from app.web import auth_handlers
