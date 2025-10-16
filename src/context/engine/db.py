from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, configure_mappers

Base = declarative_base()

class db_manager:
    def __init__(self, db_url = "sqlite:///.sqlite"):
        self.engine = create_engine(db_url)
        self.session_factory = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.SessionLocal = scoped_session(self.session_factory)


    def get_session(self):
        return self.SessionLocal()

    def init_db(self):
        from context.models.conversation import conversation
        from context.models.message import message
        configure_mappers()
        Base.metadata.create_all(bind=self.engine)

    def close_session(self):
        self.SessionLocal.remove()