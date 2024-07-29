# Функция url_for и работа с url
#
# Функция `url_for` выводит последний адрес из декоратора @app.route
#
# from flask import Flask, url_for, render_template
# 
# app = Flask('app')
# 
# @app.route('/')
# def foo():
#     print(url_for('foo')) # указывается имя функции 
#     return render_template('index.html') 
# 
# if __name__ == '__main__':
#     app.run(debug=True)
# 
# Функция url_for выводит адрес, ассоицированный с переданным в нее обработчиком
# url_for получает данные из контекста запросов
#
# from flask import Flask, url_for, render_template
# 
# app = Flask('app')
# 
# @app.route('/')
# @app.route('/index')
# def foo():
#     print(url_for('foo')) # функция вернет последний последний route ('/index') 
#     return render_template('index.html') 
# 
# if __name__ == '__main__':
#     app.run(debug=True)
#
# Flask позволяет создавать контекст запроса без запуска веб-сервера
# Делается это следующим образом
# 
# from flask import Flask, url_for, render_template
# 
# app = Flask('app')
# 
# @app.route('/')
# @app.route('/index')
# def foo():
#     return render_template('index.html') 
# 
# @app.route('/foo/<bar>')
# def bar():
#     return f'Выведу то, что ты укажешь: {bar}'
# 
# if __name__ == '__main__':
#     with app.test_request_context():
#         print(url_for('foo')) # выведется адрес без запуска веб-сервера
#
# Благодаря контексту приложения url_for корректно работает для множества
# wsgi-приложений
#
# from flask import Flask, url_for, render_template
# 
# app = Flask('app')
# 
# @app.route('/')
# @app.route('/index')
# def foo():
#     return render_template('index.html') 
# 
# @app.route('/foo/<bar>')
# def bar(bar): # сюда передается переменная, из `url`
#     return f'Выведу то, что ты укажешь: {bar}'
# 
# if __name__ == '__main__':
#     app.run(debug=True)
# 
# Существует конвертер `path`, позволяющий использовать весь оставшийся адрес
# @app.route('/profile/<path>:username') 
# Теперь что бы мы ни указали после profile оно будет обработано и передано
# например через адрес: `/profile/myname/vlad/city/mobile`
# мы в переменную username получим `/myname/vlad/city/mobile`
# без использования path мы не сможем указывать более одного адреса
# Так же существует конвертер int и float. Они позволяют указывать только 
# целочисенные или только дробные значения
