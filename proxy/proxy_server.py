import asyncio
import logging
from asyncio import futures

logger = logging.getLogger(__name__)
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 22222


class ProxyServer:
    def __init__(self):
        self._host = SERVER_HOST
        self._port = SERVER_PORT
        self._loop = asyncio.get_event_loop()
        self._server = asyncio.start_server(self.handle_connection,
                                            self._host,
                                            self._port,
                                            loop=self._loop)

    def start_server(self):
        self._server = self._loop.run_until_complete(self._server)
        logger.info(
            '***Start serving on {}***'.format(
                self._server.sockets[0].getsockname()))
        self._loop.run_forever()

    def stop_server(self):
        self._server.close()
        logger.info('***Stop server***')
        self._loop.stop()

    async def handle_connection(self, reader, writer):
        address = writer.get_extra_info('peername')
        logger.info('Accept connection from {}'.format(address))
        while True:
            try:
                data = await asyncio.wait_for(reader.read(100), timeout=5)
                if data:
                    writer.write(data)
                else:
                    logging.info(
                        'Connection from {} closed by peer'.format(address))
                    break
            except futures.TimeoutError:
                logger.info(
                    'Connection from {} closed by timeout'.format(address))
                break
        writer.close()
