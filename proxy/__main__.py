import argparse

from proxy.paths import Path
from proxy.config import update_logger_config

if __name__ == '__main__':
    path = Path()
    parser = argparse.ArgumentParser(description='Proxy server',
                                     epilog='Trubin Vitaly KB-201')
    parser.set_defaults()
    parser.add_argument('--log', '-l', default='console',
                        choices=['console', 'file'], help='logs output')
    parser.add_argument('--type', '-t', default='http',
                        choices=['http', 'https'], help='choose protocol')
    parser.add_argument('--host', '-ht', default='127.0.0.1',
                        choices=['http', 'https'], help='change protocol')
    parser.add_argument('--port', '-p', default=33333, type=int,
                        help='change protocol')

    args = parser.parse_args()

    # TODO Куда сохранять логи (Настройка абсолютного пути?)
    update_logger_config(args)

    from proxy.proxy_client import quick_start

    quick_start(args.host, args.port)

    from proxy.proxy_server import ProxyServer

    proxy_server = ProxyServer()
    proxy_server.start_server()
