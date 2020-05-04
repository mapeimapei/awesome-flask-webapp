'''
auth form表达校验处理器
'''

from wtforms import StringField, PasswordField, Form, IntegerField, validators
from wtforms.fields import html5
from wtforms.validators import Length, Email, ValidationError, EqualTo, NumberRange, Regexp,DataRequired

from app.models.auth_handlers import User

__author__ = "带土"


class LoginForm(Form):
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64), Email(message='电子邮箱不符合规范')])
    passwd = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空，请输入你的密码')])


class RegisterForm(Form):
    user_id = StringField('user_id')
    name = StringField('昵称', validators=[DataRequired(), Length(4, 10, message='昵称至少需要两个字符，最多10个字符')])

    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64), Email(message='电子邮箱不符合规范')])
    tel = StringField('tel')
    address = StringField('地址')

    passwd = PasswordField('密码', validators=[DataRequired(), Length(6, 20, message='密码长度不够')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('昵称已存在')
