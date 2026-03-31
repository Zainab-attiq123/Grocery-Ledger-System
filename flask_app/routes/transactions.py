import models

# 👤 Create User
def create_user(db, user):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 🔍 Get User
def get_user(db, username):
    return db.query(models.User).filter(models.User.username == username).first()


# 👥 Create Customer
def create_customer(db, customer):
    db_customer = models.Customer(name=customer.name, phone=customer.phone)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# 📦 Create Product
def create_product(db, product):
    db_product = models.Product(name=product.name, price=product.price, stock=product.stock)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 💰 Create Transaction
def create_transaction(db, txn):
    product = db.query(models.Product).filter(models.Product.id == txn.product_id).first()
    customer = db.query(models.Customer).filter(models.Customer.id == txn.customer_id).first()

    total = product.price * txn.quantity

    product.stock -= txn.quantity
    customer.balance += total

    db_txn = models.Transaction(
        customer_id=txn.customer_id,
        product_id=txn.product_id,
        quantity=txn.quantity,
        total_price=total
    )

    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn