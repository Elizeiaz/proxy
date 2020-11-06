import asyncio
import logging
from asyncio import futures

logger = logging.getLogger(__name__)


class ProxyClient:
    def __init__(self, proxy_host, proxy_port):
        self._proxy_host = proxy_host
        self._proxy_port = proxy_port
        self._loop = asyncio.get_event_loop()
        self._client = asyncio.start_server(self.handle_connection,
                                            self._proxy_host,
                                            self._proxy_port,
                                            loop=self._loop)

    def start_client(self):
        self._client = self._loop.run_until_complete(self._client)
        logger.info(
            '***Start serving on {}***'.format(
                self._client.sockets[0].getsockname()))
        self._loop.run_forever()

    def stop_client(self):
        self._client.close()
        logger.info('***Stop server***')
        self._loop.stop()

    async def handle_connection(self, reader, writer):
        address = writer.get_extra_info('peername')
        logger.info('Accept connection from {}'.format(address))

        try:
            from proxy.proxy_server import SERVER_HOST, SERVER_PORT
            proxy_reader, proxy_writer = await asyncio.open_connection(
                SERVER_HOST, SERVER_PORT)

            # proxy_address = proxy_writer.get_extra_info('peername')
            #
            # try:
            #     pipe_local_to_proxy = self.pipe(reader, proxy_writer)
            # except futures.TimeoutError:
            #     logger.info(
            #         'Connection from {} closed by timeout'.format(
            #             proxy_address))
            #
            # try:
            #     pipe_proxy_to_local = self.pipe(proxy_reader, writer)
            # except futures.TimeoutError:
            #     logger.info(
            #         'Connection from {} closed by timeout'.format(address))

            pipe_local_to_proxy = self.pipe(reader, proxy_writer)
            pipe_proxy_to_local = self.pipe(proxy_reader, writer)
            await asyncio.gather(pipe_local_to_proxy, pipe_proxy_to_local)
        except Exception:
            pass
        finally:
            writer.close()

    async def pipe(self, reader, writer):
        try:
            while not reader.at_eof():
                writer.write(asyncio.wait_for(reader.read(128), timeout=10))
        except futures.TimeoutError:
            return futures.TimeoutError
        finally:
            writer.close()


def quick_start(proxy_host, proxy_port):
    server = ProxyClient(proxy_host, proxy_port)
    try:
        server.start_client()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop_client()
