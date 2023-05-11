import aiomysql
import asyncio
import pymysql
from config.config import Config, load_config

config: Config = load_config('.env')
loop = asyncio.get_event_loop()


async def add_user(id_user: int, *data: dict):
    print(data)
    try:
        con = await aiomysql.connect(user=config.database.user,
                                     password=config.database.password, db=config.database.database, loop=loop)
        async with con.cursor() as cur:
            query = f"INSERT INTO users VALUES(%s, %s," \
                    f"%s, %s )"
            await cur.execute(query, (id_user, *data[0].values()))
            await con.commit()
        con.close()
    except Exception as ex:
        print(ex)


async def update_user_bd(id_user: int, *data: dict):
    try:
        con = await aiomysql.connect(user=config.database.user,
                                     password=config.database.password, db=config.database.database, loop=loop)
        async with con.cursor() as cur:
            query = 'UPDATE users SET class=%s, category=%s WHERE id_user=%s;'
            await cur.execute(query, (data[0]['clas'], data[0]['category'], id_user))
            await con.commit()
        con.close()
    except Exception as ex:
        print(ex)


async def is_user(id_user: int) -> bool:
    try:
        con = await aiomysql.connect(user=config.database.user,
                                     password=config.database.password, db=config.database.database, loop=loop)
        async with con.cursor() as cur:
            query = 'SELECT COUNT(*) FROM users WHERE id_user=%s;'
            await cur.execute(query, (id_user, ))
            result = await cur.fetchone()
        return True if int(result[0]) else False
    except Exception as ex:
        print(ex)
        return False


async def add_solution(*data: dict):
    try:
        con = await aiomysql.connect(user=config.database.user,
                                     password=config.database.password, db=config.database.database, loop=loop)
        async with con.cursor() as cur:
            query = '''
            INSERT INTO quests(text, solution, class, category)
            VALUES (%s, %s, %s, %s);
            '''
            await cur.execute(query, (data[0]['text'], data[0]['solution'], data[0]['clas'], data[0]['category']))
            await con.commit()
        con.close()
    except Exception as ex:
        print(ex)

