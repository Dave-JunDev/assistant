from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from context.engine.db import Base


class message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    role = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))

    conversation = relationship("conversation", back_populates="messages")