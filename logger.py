import logging

FORMAT = "%(asctime)s [%(name)s][%(levelname)s]  %(message)s"
logging.basicConfig(format = FORMAT, filename= "logger.log",filemode="a", level = logging.DEBUG) # by setting the level it allows that level and everything below it, default is warning, error and fatal

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.fatal("Fatal")
