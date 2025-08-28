from sqlalchemy import Column, Integer, String, Float, Date, Enum
from utils.db import Base
import enum
from datetime import date

class TransactionType(enum.Enum):
    BUY = "BUY"
    SELL = "SELL"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    stock_symbol = Column(String, nullable=False)
    shares = Column(Integer, nullable=False)
    price_per_share = Column(Float, nullable=False)
    date = Column(Date, default=date.today)
    type = Column(Enum(TransactionType), nullable=False)
