'''
auth form表达校验处理器
'''

from wtforms import StringField, PasswordField, Form, IntegerField, validators
from wtforms.fields import html5
from wtforms.validators import Length, Email, ValidationError, EqualTo, NumberRange, Regexp, DataRequired

from app.models.auth_handlers import User

__author__ = "带土"


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(6, 50, message='邮箱格式错误')])
    passwd = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空，请输入你的密码')])


class RegisterForm(Form):
    userid = StringField('userid')
    name = StringField('昵称', validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    email = StringField('email', validators=[DataRequired(), Length(6, 50, message='邮箱格式错误')])

    tel = StringField('tel')
    address = StringField('地址')

    passwd = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('昵称已存在')
