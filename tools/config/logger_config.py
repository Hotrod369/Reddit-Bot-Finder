import logging


def init_logger(file="debug.log"):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%d-%m-%y %H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(file, encoding='utf-8', delay=True),
        ],
    )
    return logging.getLogger()