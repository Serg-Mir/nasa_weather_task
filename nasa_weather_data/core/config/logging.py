from nasa_weather_data.core.config.settings import get_settings


LOGGING_LEVEL = "DEBUG" if get_settings().debug else "INFO"

logging_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "%(levelname)s: [%(name)s:%(funcName)s:%(lineno)s] %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": LOGGING_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "nasa_weather_data": {
            "handlers": ["console"],
            "propagate": False,
            "level": LOGGING_LEVEL,
        },
        "google": {
            "handlers": ["console"],
            "propagate": False,
            "level": "WARNING",
        },
        "requests": {
            "handlers": ["console"],
            "propagate": False,
            "level": "WARNING",
        },
    },
}
