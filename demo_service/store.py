from typing import AsyncGenerator, Any
from contextlib import asynccontextmanager
import aiopg

import demo_service.config as config
from demo_service.contracts import UserRequest, UserResource


_aiopg_pool: aiopg.Pool = None
async def get_engine() -> aiopg.Pool:
    global _aiopg_pool
    if _aiopg_pool is None:
        dsn = f'dbname={config.POSTGRES_DB} user={config.POSTGRES_USER} password={config.POSTGRES_PASSWORD} host={config.POSTGRES_HOST} port={config.POSTGRES_PORT}'
        _aiopg_pool = await aiopg.create_pool(dsn)
    return _aiopg_pool


async def get_users_db() -> AsyncGenerator[Any, aiopg.Connection]:
    engine = await get_engine()
    async with engine.acquire() as conn:
        yield conn


async def get_users(conn: aiopg.Connection) -> list[UserResource]:
    query = """
        SELECT id, username, first_name, last_name, birthdate
        FROM users
    """
    users = []
    async with conn.cursor() as cur:
        await cur.execute(query)
        async for row in cur:
            uid, username, first_name, last_name, birthdate = row
            user = UserResource(
                uid=uid,
                username=username,
                first_name=first_name,
                last_name=last_name,
                birthdate=birthdate,
            )
            users.append(user)
    return users
    

async def add_user(conn: aiopg.Connection, user: UserRequest) -> None:
    query = """
        INSERT INTO users (username, first_name, last_name, birthdate)
        VALUES (%s, %s, %s, %s)
    """
    async with conn.cursor() as cur:
        await cur.execute(query, (user.username, user.first_name, user.last_name, user.birthdate))
        conn.commit()