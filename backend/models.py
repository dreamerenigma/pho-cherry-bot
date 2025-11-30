from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(JSONB, nullable=False) 
    description = Column(JSONB, nullable=True)
    weight = Column(JSONB, nullable=True) 
    price = Column(Float, nullable=False)
    image = Column(String, nullable=True)