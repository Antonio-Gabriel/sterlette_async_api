from orm import Model, Integer, String
from src.config.databases import database, metadata


class User(Model):
    __tablename__ = 'users'
    __database__ = database
    __metadata__ = metadata

    id = Integer(primary_key=True)
    name = String(allow_null=False, max_length=100)
    email = String(allow_null=False, unique=True, index=True, max_length=84)
    password = String(allow_null=False, max_length=255)

    def __repr__(self):
        return f"User: {self.name}"
