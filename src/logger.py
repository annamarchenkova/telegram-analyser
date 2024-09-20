import logging, hashlib, structlog


def configure_logger(verbosity=0):
    """Configure the logger with a given verbosity level."""

    log_level = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}[verbosity]

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(log_level))

logger = structlog.get_logger()
