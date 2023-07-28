import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.CRITICAL)
    logger.debug("Debug")
    logger.info("Info")
    logger.critical("critical")
    logger.error("Error")
    logger.warning("Warning")
