from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Cafe(Base):
    __tablename__ = 'cafe'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(2048))
    precio: Mapped[float] = mapped_column()