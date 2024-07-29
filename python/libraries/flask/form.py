# Подключение ресурсов и работа с формами
# url_for('static', filename='css/styles.css') - обращение к директории static 
# и css/styles.css внутри директории static. Папка static должна находиться на 
# одном уровне вложенности с приложением. 
# При работе с формами Flask передает данные через ImmutableDict. 
# Получить доступ к данным можно примерно следующим способом:
# request.form или же request.form['field_name']
