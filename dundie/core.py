"""Core module of dundie"""
from dundie.utils.log import get_loggers

log = get_loggers()


def load(filepath):
    """Load data from filepath to database."""
    try:
        with open(filepath) as file_:
            return file_.readlines()
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
