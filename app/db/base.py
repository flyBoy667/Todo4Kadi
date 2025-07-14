from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql://postgres:root@localhost/todo4kadi")


Base = declarative_base()


from app.models import User, Todo
