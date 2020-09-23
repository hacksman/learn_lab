# coding: utf-8
# @Time : 2020/9/17 8:59 AM

from loguru import logger

import time
import os.path
import asyncio
import click
import websockets
from collections import deque
from urllib.parse import urlparse, parse_qs
from ansi2html import Ansi2HTMLConverter

NUM_LINES = 1000
HEARTBEAT_INTERVAL = 10  # seconds

allowed_prefixes = ["/Users/x/study/python/learn_lab/logs"]
conv = Ansi2HTMLConverter(inline=True)


async def view_log(websocket, path):

    logger.info(f'Connected, remote={websocket.remote_address}, path={path}')

    try:
        try:
            parse_result = urlparse(path)
        except Exception:
            raise ValueError('Fail to parse URL')

        file_path = os.path.abspath(parse_result.path)
        logger.info(file_path)
        allowed = False
        for prefix in allowed_prefixes:
            if file_path.startswith(prefix):
                allowed = True
                break
        if not allowed:
            raise ValueError('Forbidden')

        if not os.path.isfile(file_path):
            raise ValueError('Not found')

        query = parse_qs(parse_result.query)
        tail = query and query['tail'] and query['tail'][0] == '1'

        with open(file_path) as f:

            content = ''.join(deque(f, NUM_LINES))
            content = conv.convert(content, full=False)
            await websocket.send(content)

            if tail:
                last_heartbeat = time.time()
                while True:
                    content = f.read()
                    if content:
                        content = conv.convert(content, full=False)
                        await websocket.send(content)
                    else:
                        await asyncio.sleep(1)

                    # heartbeat
                    if time.time() - last_heartbeat > HEARTBEAT_INTERVAL:
                        try:
                            await websocket.send('ping')
                            pong = await asyncio.wait_for(websocket.recv(), 5)
                            logger.info(f"pong:{pong}")
                            if pong != 'pong':
                                raise Exception()
                        except Exception:
                            raise Exception('Ping error')
                        else:
                            last_heartbeat = time.time()

            else:
                await websocket.close()

    except ValueError as e:
        try:
            await websocket.send('<font color="red"><strong>{}</strong></font>'.format(e))
            await websocket.close()
        except Exception as e:
            pass
        logger.info(f"value error happen: {e}")
        log_close(websocket, path, e)

    except Exception as e:
        logger.info(f"Exception error happen: {e}")
        log_close(websocket, path, e)

    else:
        log_close(websocket, path)


def log_close(websocket, path, exception=None):
    message = 'Closed, remote={}, path={}'.format(websocket.remote_address, path)
    if exception is not None:
        message += ', exception={}'.format(exception)
    logger.info(message)


@click.command()
@click.option("--host",
              type=str,
              default="127.0.0.1",
              help="websocket remote host")
@click.option("--port",
              type=int,
              default=8765,
              help="websocket remote port")
def main(host, port):
    start_server = websockets.serve(view_log, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
