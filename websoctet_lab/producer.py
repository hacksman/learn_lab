# coding: utf-8
# @Time : 2020/9/15 8:42 AM

import asyncio
import websockets


async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()


if __name__ == '__main__':
    asyncio.run(produce("hi", "127.0.0.1", 4000))
