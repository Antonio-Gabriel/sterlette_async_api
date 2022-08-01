from uvicorn import run

from sqlalchemy import create_engine
from starlette.applications import Starlette

from src.routes import routes
from src.config.databases import database, metadata

engine = create_engine(str(database.url))
metadata.create_all(engine)

app = Starlette(debug=True, routes=routes,
                on_startup=[database.connect], on_shutdown=[database.disconnect])

if __name__ == "__main__":
    run("run:app", reload=True, port=5000, host='0.0.0.0')
