from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=35)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Вход')

class EditProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Пароль', validators=[
        DataRequired(),
        Length(min=2, max=20),
        EqualTo('confirm_password', message='Пароли должны совпадать')
    ])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменения')