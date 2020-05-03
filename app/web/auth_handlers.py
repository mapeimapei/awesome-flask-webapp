'''
user handlers
'''
from . import web
from ..forms.auth_handlers import RegisterForm
from ..libs.util import next_id

from flask import render_template, flash, request, jsonify, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user
from app.models import db
from ..models.auth_handlers import User
import time, logging

from flask_sqlalchemy import get_debug_queries

logging.basicConfig(level=logging.DEBUG)

__author__ = "带土"


# 这里需要优化
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

    # form = RegisterForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     user = User()
    #     user.set_attrs(form.data)
    #     db.session.add(user)
    #     db.session.commit()
    #     # token = user.generate_confirmation_token()
    #     # send_email(user.email, 'Confirm Your Account',
    #     #            'email/confirm', user=user, token=token)
    #     login_user(user, False)
    #     # flash('一封激活邮件已发送至您的邮箱，请快完成验证', 'confirm')
    #     # 由于发送的是ajax请求，所以redirect是无效的
    #     # return render_template('index.html')
    #     return redirect(url_for('web.index'))
    # return render_template('auth/register.html', form=form)
