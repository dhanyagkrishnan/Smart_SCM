from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    product_name = Column(String, nullable=False)
    stock = Column(Integer, default=0)
    reorder_level = Column(Integer, default=0)
    daily_demand = Column(Integer, default=0)
    unit_cost = Column(Float, default=0.0)

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sku = Column(String, index=True, nullable=False)
    lead_time_days = Column(Integer, default=0)
    reliability = Column(Float, default=0.0)
    unit_price = Column(Float, default=0.0)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, index=True, nullable=False)
    quantity = Column(Integer, default=0)
    status = Column(String, default="Pending")
    supplier = Column(String, default="")
    expected_date = Column(String, default="")
