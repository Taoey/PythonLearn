#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
from datetime import datetime


async def add(a, b):
    await asyncio.sleep(1)
    return a + b


async def master_thread(loop):
    print("{} master: 1+2={}".format(datetime.now(), await add(1, 2)))


def slave_thread(loop):
    # 注意：这不是 coroutine 函数
    import time
    time.sleep(2)

    f = asyncio.run_coroutine_threadsafe(add(1, 2), loop)
    print("{} slave: 1+2={}".format(datetime.now(), f.result()))


async def main(loop):
    await asyncio.gather(
        master_thread(loop),
        # 线程池内执行
        loop.run_in_executor(None, slave_thread, loop),
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()