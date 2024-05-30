from sqlalchemy import Column, Integer, String, true
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from connection import engine

class Base(DeclarativeBase):
    pass


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int]  = mapped_column(primary_key=True,nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    login: Mapped[str] = mapped_column(String(30), nullable= False, unique=True) 
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    #password = Column(String(255), unique=True, nullable=False)

class Account(Base):
    __tablename__ = "account"

    account_number: Mapped[int]  = mapped_column(primary_key=True,nullable=False)
    balance: Mapped[float] = mapped_column(String(30), nullable=False)
    id_client: Mapped[str] = mapped_column(String(30), nullable= False, unique=True) 
    password: Mapped[str] = mapped_column(String(30), nullable=False)


# Criando as tabelas no banco de dados (se ainda não existirem)
Base.metadata.create_all(engine)
