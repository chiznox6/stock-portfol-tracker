from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Use relative path for SQLite (creates portfolio.db in project root)
DATABASE_URL = "sqlite:///./portfolio.db"

# Base class for models
Base = declarative_base()

# SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, echo=False, future=True
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency helper for session management
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
