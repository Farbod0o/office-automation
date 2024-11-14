import logging
import sys

class Logger:
    logging.basicConfig(
        level=logging.DEBUG,  # سطح لاگ را به DEBUG تغییر دادیم تا همه پیام‌ها ثبت شوند
        format="%(asctime)s - %(levelname)5s - %(message)s",
        encoding="UTF-8",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    @classmethod
    def info(cls, message):
        logging.info(message)

    @classmethod
    def error(cls, message, exc_info=False):
        logging.error(message, exc_info=exc_info)

    @classmethod
    def debug(cls, message):
        logging.debug(message)
