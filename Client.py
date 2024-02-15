import asyncio
import aiohttp
import random
import time


class DummyMessengerClient:
    def __init__(self):
        self.urls = ['http://localhost:8080/messages', 'http://localhost:8080/messages']
        self.names = ['Ховар', 'Ваня', 'Саша', 'Маша', 'Настя', 'Ася', 'Алекс', 'Илья', 'Дима', 'Таня']

    async def send_messages(self, session):
        sender = random.choice(self.names)
        message = {'sender': sender, 'text': 'Hello, World!'}
        async with session.post(random.choice(self.urls), json=message) as response:
            await response.json()

    async def main(self):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            await asyncio.gather(*[self.send_messages(session) for _ in range(5000)])
            end_time = time.time()
            elapsed_time = end_time - start_time
            avg_request_time = elapsed_time / 5000
            throughput = 5000 / elapsed_time
            print(f'Total: {elapsed_time} seconds')
            print(f'Average: {avg_request_time} seconds')
            print(f'Per/sec: {throughput} requests/second')


async def run_client():
    client = DummyMessengerClient()
    await client.main()


asyncio.run(run_client())
