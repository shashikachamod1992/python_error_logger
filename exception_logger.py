import logging
from datetime import datetime
import traceback

LOG_FILENAME = 'error_log.out'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


def log_exceptions(exception_traceback):
    now = datetime.now()
    message = '\n' + '\n'+ '\n' + now.strftime(
        "%m/%d/%Y, %H:%M:%S") +'\n'+ exception_traceback + '\n'
    logging.exception(message)


if __name__ == '__main__':
    try:
        x = 5 / 0
    except:
        log_exceptions(str(traceback.format_stack()))


