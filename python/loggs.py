# Лог - важная запись из жизненного цикла программы
# В python за логирование отвечает модуль logging

import logging

# в python есть пять уровней логирования --- от самого низкого уровня,
# до самого высокого:
# debug --- самый низкий уровень логирования, предназначенный для 
# отладочных сообщений 
# info --- выводит информацию, подобно print
# warning --- выводит предупреждения, на которые стоит обратить внимание
# По умолчанию logging использует этот уровень
# error --- выводит ошибки в том случае, если программа ведет себя не так,
# как ожидается --- программа не смогла правильно выполниться
# critical --- самый высокий уровень логирования. Выводятся ошибки, нарушающие
# работу приложения и ломающие его

logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

# WARNING:root:A WARNING
# ERROR:root:An ERROR
# CRITICAL:root:A message of CRITICAL severity
# debug, info не выводятся в консоль

# Для настройки конфигурации логера используется basicConfig

logging.basicConfig(level=logging.INFO,
                    filename="py_log.log",
                    filemode="w", 
                    format="%(asctime)s %(levelname)s %(message)s"
                    )

# level --- уровень на котором начинается логирование
# filename --- имя файла, куда мы будем писать логи
# filemode --- необязательный параметр. Указываем как будем писать логи. По умолчанию стоит "a"
# format --- формат для записи логов. 

# Для вызова стек-трейса используется параметр exc_info. По умолчанию он стоит False. 

x = 4
y = 0

logging.info(f"The values of x and y are {x} and {y}.")
try:
    x/y
    logging.info(f"x/y successful with result: {x/y}.")
except ZeroDivisionError as err:
    logging.error("ZeroDivisionError",exc_info=True)


# Для получения диагностической информации в продакшене используют sentry-sdk
# Для инициализации sentry используется следующий код:

sentry_sdk.init(
     dsn="<your-dsn-key-here>",
     traces_sample_rate=0.85,
)

# dsn получают при создании проекта внутри sentry. 

