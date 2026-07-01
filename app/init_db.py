from app.database import engine
from app.models.article import Base

Base.metadata.create_all(
    bind=engine
)

print("Database initialization successful")
