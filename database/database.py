import asyncio
import sys
import psycopg
from dotenv import load_dotenv

load_dotenv('.env')


class Database:
    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = None
        self.cur = None

    async def connection(self):
        """
        this func connect database
        :return:
        """
        self.conn = await psycopg.AsyncConnection.connect(
            f"dbname={self.dbname} user={self.user} password={self.password} host='localhost'")
        self.cur = self.conn.cursor()

    # async def check_user(self, user_id):
    #     await self.cur.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
    #     res = await self.cur.fetchone()
    #     if res:
    #         return True
    #     else:
    #         return False


if __name__ == '__main__':
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
