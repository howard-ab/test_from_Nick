import asyncio
from aiohttp import web
import asyncpg
import json
from datetime import datetime


class DummyMessengerServer:
    def __init__(self):
        self.app = web.Application()
        self.app.router.add_post('/messages', self.handle_post)
        self.pool = None

    async def init_db(self):
        self.pool = await asyncpg.create_pool(user='howard', password='01234',
                                              database='mydatabase', host='localhost')

        async with self.pool.acquire() as conn:
            await conn.execute('''
            create table if not exists message 
            (id integer primary key,
            sender text not null,
            text text not null,
            sent_at timestamp default current_timestamp)
            ''')

    async def handle_post(self, request):
        data = await request.json()
        sender = data.get('sender')
        text = data.get('text')

        async with self.pool.acquire() as conn:
            await conn.execute('''insert into messages (sender, text) values ($1, $2)''', sender, text)

            messages = await conn.fetch('''select * from messages order by id desc LIMIT 10''')

        messages_json = [{'sender': row['sender'], 'text': row['text'], 'sent_at': row['sent_at'].isoformat()} for row
                         in messages]

        return web.json_response(messages_json)

    async def start(self):
        await self.init_db()
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8080)
        await site.start()

        print("Server started at http://localhost:8080")

        while True:
            await asyncio.sleep(3600)

    async def stop(self):
        await self.pool.close()


async def run_server():
    server = DummyMessengerServer()
    await server.start()


asyncio.run(run_server())