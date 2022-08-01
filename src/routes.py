from starlette.routing import Route, Mount

from src.controllers import user_controller, home_controller

routes = [
    Route('/', endpoint=home_controller.home),
    Mount('/users', routes=[
        Route('/', endpoint=user_controller.users)
    ])
]
