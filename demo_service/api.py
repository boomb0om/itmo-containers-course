from http import HTTPStatus
from typing import Annotated
import os
import aiopg

from fastapi import FastAPI, HTTPException, Query, Response, Depends

from demo_service import store
from demo_service.contracts import UserRequest, UserResource, UserList
from demo_service.store import get_users_db, get_users, add_user


app = FastAPI(title="Demo User API")


@app.post(
    "/users/add",
    status_code=HTTPStatus.CREATED,
)
async def create_user(
    body: UserRequest,
    conn: Annotated[aiopg.Connection, Depends(get_users_db)]
) -> UserRequest:
    await add_user(conn, body)
    return body


@app.get(
    "/users/list",
    status_code=HTTPStatus.OK,
)
async def list_users(
    conn: Annotated[aiopg.Connection, Depends(get_users_db)]
) -> UserList:
    users = await get_users(conn)
    return UserList(users=users)

