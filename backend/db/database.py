from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.config import settings


engine=create_engine(settings.DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()

        # return db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(engine)



