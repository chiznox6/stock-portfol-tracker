from sqlalchemy import Column, Integer, String, Float
from utils.db import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    target_value = Column(Float, nullable=False)
