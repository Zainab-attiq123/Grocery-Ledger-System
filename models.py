from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

# 👤 User Table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

# 👥 Customer Table
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    balance = Column(Float, default=0.0)

# 📦 Product Table
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

# 💰 Transaction Table
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    total_price = Column(Float)
