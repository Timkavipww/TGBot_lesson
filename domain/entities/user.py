from infrastructure.database import Base
from sqlalchemy import (
    BigInteger, 
    Column, 
    DateTime, 
    String
)

from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement="ignore_fk")
    username = Column(String(32), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())