from flask import Flask, render_template
app = Flask(__name__)



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





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
