# coding: utf-8
# @Time : 2020/9/15 9:17 AM

import asyncio
import websockets
from websockets import WebSocketClientProtocol
from loguru import logger


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    async for message in websocket:
        log_message(message)
        if message == "ping":
            await websocket.send("pong")


async def cousume(hostname: str, port: int, log_file: str, tail:bool=True) -> None:
    websocket_resource_url = f"ws://{hostname}:{port}{log_file}"
    if tail:
        websocket_resource_url = f"{websocket_resource_url}?tail=1"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)


def log_message(message: str) -> None:
    logger.info(f"Message: {message}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cousume("127.0.0.1", 8765, "/Users/x/study/python/learn_lab/logs/logger_extend.log"))
    loop.run_forever()
