# Мгновенные сообщения
#
# Для отправки мгновенных сообщений клиенту Flask использует функцию flash()
# для отправки клиенту шаблона с сообщением используется функция
# get_flashed_messages()
#
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'foobaaaaaar' # шифрование при помощи секретного ключа

menu = [
    {"name": "Установка", "url": "install-flask"},
    {"name": "Первое приложение", "url": "install-app"},
    {"name": "Обратная связь", "url": "constact"},
]

@app.route('/')
def index():
    return render_template('index.html', menu = menu)

@app.route('/about')
def about():
    return render_template('about.html', title = 'О сайте', menu = menu)

@app.route('/contact', methods=['POST','GET'])
def contacts():
    if request.method == 'POST':
        print(request.form['username'])

if __name__=='__main__':
    app.run(debug=True)
