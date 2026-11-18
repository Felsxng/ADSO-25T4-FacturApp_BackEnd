from sqlalchemy import Column, Integer, String
from src.models import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    active = Column(Integer, default=1)  # 1 for active, 0 for inactive

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', description='{self.description}')>"