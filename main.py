import asyncio
import logging

from src import app

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    asyncio.run(app.run())
