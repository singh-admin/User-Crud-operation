from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI = "sqlite:///./user.db"

#engine instance for integerate the database api connection.
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, echo=True
)

# create a SessionLocal instance for database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# this function return the a class so after inherit the base class we can create a each database Models(ORM).
Base = declarative_base()


# Dependency of making a connection with sql database.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()