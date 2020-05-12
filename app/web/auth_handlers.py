'''
user handlers
'''
from sqlalchemy import or_
from wtforms import form

from app.web import web
from app.forms.auth_handlers import RegisterForm, LoginForm
from ..libs.util import next_id

from flask import render_template, flash, request, jsonify, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user
from app.models.base import db
from app.models.auth_handlers import User
import time, logging

from flask_sqlalchemy import get_debug_queries

logging.basicConfig(level=logging.DEBUG)

__author__ = "带土"

@web.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        try:
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, False)

        except Exception as e:
            db.session.rollback()
            raise e
        return redirect(url_for('web.index'))
    return render_template('register.html', form=form)


@web.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.passwd.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误', category='login_error')

    return render_template('login.html', form=form)


@web.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))




