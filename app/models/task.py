import uuid
from sqlalchemy import Column, String, datetime
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.sql import func

from app.models.base import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(String, primary_key= True, default= lambda: str(uuid.uuid4()))
    type = Column(String, nullable=False)
    status = Column(String, default= "pending")
    result = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())