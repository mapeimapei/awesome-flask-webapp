'''
user handlers
'''
from wtforms import form

from . import web
from ..forms.auth_handlers import RegisterForm, LoginForm
from ..libs.util import next_id

from flask import render_template, flash, request, jsonify, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user
from app.models import db
from ..models.auth_handlers import User
import time, logging

from flask_sqlalchemy import get_debug_queries

logging.basicConfig(level=logging.DEBUG)

__author__ = "带土"



@web.route("/register2", methods=["GET", "POST"])
def register2():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.index'))

    return render_template('register2.html', form=form)


@web.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.passwd.data):
            #login_user(user, remember=True)
            print('ook ',user )
            return redirect(url_for("web.index"))
        else:
            flash('账号不存在或密码错误', category='login_error')
    return render_template('login.html')


    # form = LoginForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and user.check_password(form.password.data):
    #         login_user(user, remember=True)
    #         next = request.args.get('next')
    #         if not next or not next.startswith('/'):
    #             next = url_for('web.index')
    #         return redirect(next)
    #     else:
    #         flash('账号不存在或密码错误', category='login_error')






