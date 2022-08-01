from databases import Database
from sqlalchemy import MetaData

database = Database("sqlite:///starlette.db")
metadata = MetaData()
