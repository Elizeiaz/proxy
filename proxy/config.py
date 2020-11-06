import logging
from proxy.paths import Path


# TODO add default logger
def update_logger_config(args):
    if args.log == 'file':
        logging.basicConfig(filename="log.txt", filemode="a+",
                            level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - '
                                   '%(message)s')
    elif args.log == "console":
        logging.basicConfig(level=logging.INFO,
                            format='%(name)s - %(levelname)s - '
                                   '%(message)s')
