from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from app import api as studentapi

app = FastAPI()
app.include_router(studentapi.app, tags =['studentapi'])

register_tortoise(
    app,
    db_url="mysql://root:root@127.0.0.1/studentDetail",  # MySQL URL format
    modules={'models': ['app.models']}, 
    generate_schemas=True, #for generate schema in database
    add_exception_handlers=True 
)