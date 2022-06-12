import logging
import os
import json
from typing import Dict

PROJECT_NAME = "news-sn-scraper"
LOG_FILE = PROJECT_NAME + ".log"
BASE_DIR = os.getcwd()
SELECTORS_FILE = os.path.join(BASE_DIR, "src", "selectors.json")


def log(func):
    """Decorator to log functions"""

    def wrapper(*args, **kwargs):
        logger = logging.getLogger(PROJECT_NAME)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(LOG_FILE)
        fmt = "%(asctime)s - %(name)s - %(message)s"
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.info(f"Running function: {func.__name__} with args: {args}")
        return func(*args, **kwargs)

    return wrapper


def _load_file() -> dict:
    with open(SELECTORS_FILE, "r") as f:
        selectors = json.loads(f.read())
    return selectors


@log
def get_selectors(website: str) -> Dict[str, str]:
    """Get selectors of a website"""
    try:
        return _load_file().get(website)
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    selectors = get_selectors("dakaractu")
    print(selectors)
