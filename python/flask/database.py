import sqlite3
import os
from flask import Flask, render_template, request

# configuration
DEBUG = True
DATABASE = 'home/yazop/my_db.db'
SECRET_KEY = 'foobarbiz'

app = Flask(__name__)
app.config.from_object(__name__) # указываем откуда берем конфигурацию приложения

# т.к. я могу иметь несколько wsgi-приложений, то имеет смысл переопределить
# путь базы данных
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'foobar.db')))

# для вызова базы данных используется модуль sqlite3

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn
    # используется для представления данных не в виде кортежа,а в виде словаря

def create_db():
    '''Вспомогательная функция для создания таблиц БД'''
    db = connect_db()

