from starlette.requests import Request
from starlette.responses import JSONResponse


async def home(request: Request):
    return JSONResponse({"msg": 'Welcome to api'})
