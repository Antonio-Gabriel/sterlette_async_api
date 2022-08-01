from starlette.requests import Request
from starlette.responses import JSONResponse

from src.Models.models import User


async def users(request: Request):
    contents = await User.objects.all()
    results = [
        {
            "id": content.id,
            "name": content.name,
            "email": content.email
        }
        for content in contents
    ]

    return JSONResponse(results)
 