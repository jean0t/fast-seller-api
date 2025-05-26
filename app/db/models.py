from sqlalchemy import ForeignKey
from sqlalchemy import String, Column, Integer, Boolean, DateTime, LargeBinary, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


#===========================================================================| Client

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    orders = relationship("Order", back_populates="client")


#===========================================================================| Product

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    section = Column(String, nullable=False)
    bar_code = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(DateTime, nullable=True)
    available = Column(Boolean, nullable=False)

    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    orders = relationship("Order", secondary="order_product", back_populates="products")


class ProductImage(Base):
    __tablename__ = "product_images"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    image = Column(LargeBinary, nullable=False)
    product = relationship("Product", back_populates="images")



#===========================================================================| Orders


class OrderProduct(Base):
    __tablename__ = "order_product"

    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)



class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)

    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    client = relationship("Client", back_populates="orders")

    products = relationship("Product", secondary="order_product", back_populates="orders")
