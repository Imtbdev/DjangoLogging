import logging
from django.http import HttpResponse

logger = logging.getLogger("Logg_app")


def log_example_view(request):
    logger.debug("Это DEBUG сообщение — отладочная информация")
    logger.info("Это INFO сообщение — общее уведомление")
    logger.warning("Это WARNING сообщение — предупреждение")
    logger.error("Это ERROR сообщение — ошибка")
    logger.critical("Это CRITICAL сообщение — критическая ошибка")

    return HttpResponse("Логирование выполнено. Проверь файл `project.log` и консоль.")
