# При получении сервером запроса от клиент: создается контекст приложения,
# после чего создается контекст запроса.
#
# Контекст приложения содержит в себе две переменные: `g` и `current_app`.
# Данные переменные хранятся в контексте одного запроса - после они очищаются
# Если нам не нужен функционал контекста приложения, то оно может не создаваться
# Это делается чтобы экономить ресурсы процессора
#
# В свою очередь контекст запроса создается `всегда`. В себе он содержит
# `request` и `session`. При появлении запроса активируется поток обработки 
# запроса, и в пределах данного потока может быть доступна переменная `request`
# Для каждого запроса создается свой поток, содержащий свою переменную `request`
# `session` - словарь, в котором можно сохранять данные в пределах сессии. 
# То есть сессия хранится все время работы приложения. 
# `session` имеет срок жизни. 
