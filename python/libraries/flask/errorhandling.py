# Декоратор errorhandler, функция redirect и abort
#
# redirect - перенаправляет на другой адрес, например redirect('/foo')
# 
# abort - прерывает запрос, например abort(401)
# 
# Декортатор errorhandler принимает на вход аргумент с значением ошибки
# Функция должна принимать на вход в качестве аргумента ошибку
# @app.errorhandler(404)
# def page_not_found(error):
#   return render_template('page404.html')
