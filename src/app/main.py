from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class Param(str, Enum):
    A = "a"
    B = "b"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{param}")
async def root_with_param(param):
    return {"message": f"Hello {param}"}


@app.get("/param/{enum_param}")
async def param_basic_test(enum_param: Param):
    if enum_param == Param.A:
        return {"message": f"Hello {enum_param.name}"}
