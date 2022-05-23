import logging

#日志打印
def login_info(info):
    logger = logging.getLogger(__name__)
    logger.info(info)