# -*- coding: utf-8 -*-

import logging
import constant
import  config


def init_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(constant.LOG_PATH)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def convert_readable_text(text):
    lower_text = text.lower()

    if lower_text.endswith("k"):
        return int(text[:-1]) * 1024

    if lower_text.endswith("m"):
        return int(text[:-1]) * 1024 * 1024

    if lower_text.endswith("g"):
        return int(text[:-1]) * 1024 * 1024 * 1024
    return 0
