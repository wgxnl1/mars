from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template
from flask import redirect
from flask import Flask
from flask import request

app = Flask(__name__)
class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def index123():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def promt():
    return (f'Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>'
            f'Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!')


@app.route('/image_mars')
def mars():
    return render_template('index.html')

@app.route('/promotion_image')
def promim():
    return render_template('promim.html')
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astro():
    if request.method == 'GET':
        return render_template('astronaut_selection.html')
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

@app.route('/<title>')
@app.route('/index/<title>')
def kosms(title):
    return render_template('index1.html', title=title)

class AutoLoginForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    education = StringField('Образование', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = StringField('Пол', validators=[DataRequired()])
    motivation = StringField('Мотивация', validators=[DataRequired()])
    ready = BooleanField('Готовы ли вы остаться на Марсе?')
    submit = SubmitField('Войти')


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def answer():
    form = AutoLoginForm()
    if form.validate_on_submit():
        return render_template('success.html', form=form)
    return render_template('login.html', title='Авторизация', form=form)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
