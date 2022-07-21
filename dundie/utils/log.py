import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.getLogger("dundie")

fmt = logging.Formatter(
    "%(ascime)s %(name)s %(levelname)s " "1:%(lileno)d f:%(filename)s: %(message)s"
)


def get_loggers(logfile="dundie.log"):
    """Returns a configured logger."""
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=300,
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log