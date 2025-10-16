from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from context.engine.db import Base


class conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    messages = relationship("message", back_populates="conversation", cascade="all, delete-orphan")