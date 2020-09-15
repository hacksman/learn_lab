# coding: utf-8
# @Time : 2020/9/15 9:17 AM

import asyncio
import websockets
from websockets import WebSocketClientProtocol
from loguru import logger


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    async for message in websocket:
        log_message(message)


async def cousume(hostname: str, port: int) -> None:
    websocket_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)


def log_message(message: str) -> None:
    logger.info(f"Message: {message}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cousume("127.0.0.1", 4000))
    loop.run_forever()
