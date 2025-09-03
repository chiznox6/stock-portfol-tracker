from sqlalchemy import Column, Integer, Float, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from models.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    shares = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    type = Column(Enum("buy", "sell", name="transaction_type"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, symbol={self.symbol}, shares={self.shares}, price={self.price}, type='{self.type}', user_id={self.user_id})>"
