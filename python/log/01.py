import logging
LOG_FORMAT = "%(asctime)s----%(levelname)s----%(message)s"

# 简单的配置。
logging.basicConfig(filename="logfile.log", level=logging.DEBUG, format=LOG_FORMAT)


logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")

logging.basicConfig(level=logging.WARNING)  # 没有作用。
# 另外一种写法
logging.log(logging.DEBUG, "this is a dubug log")
logging.log(logging.WARNING, "this is a WARINING log")