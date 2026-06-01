from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.db.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base = declarative_base()

from app.models import User, Todo  # noqa: E402, F401
