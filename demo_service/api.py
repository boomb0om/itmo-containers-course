from http import HTTPStatus
from typing import Annotated
import os
import psycopg2

from fastapi import FastAPI, HTTPException, Query, Response
from prometheus_fastapi_instrumentator import Instrumentator

from demo_service import store
from demo_service.contracts import UserRequest, UserResource

app = FastAPI(title="Demo User API")
Instrumentator().instrument(app).expose(app)


@app.post(
    "/create-user",
    response_model=UserResource,
    status_code=HTTPStatus.CREATED,
)
async def create_user(body: UserRequest) -> UserResource:
    return store.insert(body)


@app.get(
    "/",
    response_model=UserResource,
    status_code=HTTPStatus.CREATED,
)
async def create_user() -> Response:
    postgres_user = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    postgres_db = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')

    conn = psycopg2.connect(
        dbname=postgres_db,
        user=postgres_user,
        password=postgres_password,
        host=host,
        port=port
    )
    with conn.cursor() as cur:
        cur.execute("select * from Users")
        print(cur.fetchall())
    return Response()


@app.post("/get-user")
async def get_user(id: Annotated[int, Query()]) -> UserResource:
    resource = store.select(id)

    if not resource:
        raise HTTPException(HTTPStatus.NOT_FOUND)

    return resource
