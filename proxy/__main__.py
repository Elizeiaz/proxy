import logging.config
import argparse

from proxy.paths import Path

if __name__ == '__main__':
    path = Path()

    parser = argparse.ArgumentParser()
    parser.add_argument("--log", "-l", default="213", help="print logs")
    args = parser.parse_args()

    logging.config.fileConfig(path.log_properties)

    from proxy.proxy_server import main

    main()
