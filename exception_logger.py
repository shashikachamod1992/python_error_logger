import logging
from datetime import datetime

LOG_FILENAME = 'error_log.out'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


def log_exceptions(log_no, exception_traceback):
    now = datetime.now()
    message = '\n' + '\n' + 'Log no - ' + log_no + '\n' + now.strftime(
        "%m/%d/%Y, %H:%M:%S") +'\n'+ exception_traceback + '\n'
    logging.exception(message)
