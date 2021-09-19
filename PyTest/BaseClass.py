import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # to print the actual file name where it is called not baseclass file name
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile1.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
