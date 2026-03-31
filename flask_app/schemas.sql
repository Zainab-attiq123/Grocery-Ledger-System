from pydantic import BaseModel

# 👤 User
class UserCreate(BaseModel):
    username: str
    password: str

# 👥 Customer
class CustomerCreate(BaseModel):
    name: str
    phone: str

# 📦 Product
class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

# 💰 Transaction
class TransactionCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int