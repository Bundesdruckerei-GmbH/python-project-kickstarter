"""Copyright 2025 Bundesdruckerei GmbH.

Licensed under Apache-2.0, see the accompanying file LICENSE

Define general logging handling.
"""

import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": (
                "%(asctime)s %(levelname)s %(name)s %(module)s "
                "%(lineno)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S.%f%:z",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": "DEBUG",
        }
    },
    "loggers": {
        "root": {"level": "INFO", "handlers": ["console"]},
        "__main__": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
    },
}


def setup_logging() -> None:
    """Set up logging configuration."""
    logging.config.dictConfig(LOGGING_CONFIG)
