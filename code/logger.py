# # library
import logging
import traceback


class Logger(object):

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self._console()
        self._file()

    def _console(self):
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        format_log = logging.Formatter('%(message)s')
        handler.setFormatter(format_log)

        self.logger.addHandler(handler)

    def _file(self):
        handler = logging.FileHandler('logger.log')
        handler.setLevel(logging.ERROR)
        format_log = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n'
                                       '------------------------------------------------------------------------------')
        handler.setFormatter(format_log)

        self.logger.addHandler(handler)

    def warning(self) -> str:
        self.logger.warning('The error is written to the logger.log file')

        return 'ERROR! The error is written to the logger.log file'

    def error(self):
        self.logger.error(traceback.format_exc())
